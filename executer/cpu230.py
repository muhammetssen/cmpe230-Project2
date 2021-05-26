import functions


class Cpu230:
    flags = {
        "ZF": False,
        "CF": False,
        "SF": False,
        ##
        "JF": False # We jumped
    }
    registers = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "S": 64 * 1024 - 1,
        "PC": 0
    }

    memory = [None] * 

    def instructionsToMemory(self, instructions):
        count = 0
        for instruction in instructions:
            self.memory[count] = instruction[0:8]
            count += 1
            self.memory[count] = instruction[8:16]
            count += 1
            self.memory[count] = instruction[16:]
            count += 1
    def writeToMemory(self, value): # Value is expected to be a decimal
        CHUNK_SIZE = 8
        a = format(value,"08b")
        b = "0"* (CHUNK_SIZE - len(a) % CHUNK_SIZE) + a
        for i in range(len(b) / CHUNK_SIZE):
            #TODO check for stackoverflow
            self.memory[self.registers['S']] = b[i*CHUNK_SIZE:(i+1)*CHUNK_SIZE]
            self.registers['S']-=1
    
    def readFromMemory(self, index):
        return int(self.memory[index] + self.memory[index-1],2)

    def run(self):
        while True:
            # 24 bits string
            self.flags['JF'] = False
            currentInstruction = self.memory[self.registers["PC"]] + self.memory[self.registers["PC"] + 1] + self.memory[self.registers["PC"] + 2]
            instructionDetails = functions.GNUToBinary(currentInstruction)
            selectedFunction, address_mode, operand = instructionDetails
            a = functions.functionCodes[selectedFunction](self, address_mode, operand)
            if not self.flags['JF']:
                self.registers['PC'] += 3
            
