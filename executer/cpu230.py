import functions


class Cpu230:
    flags = {
        "ZF": False,
        "CF": False,
        "SF": False,
        ##
        "JF": False  # We jumped
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

    memory = [None] * 64 * 1024

    def instructionsToMemory(self, instructions):
        count = 0
        for instruction in instructions:
            self.memory[count] = instruction[0:8]
            count += 1
            self.memory[count] = instruction[8:16]
            count += 1
            self.memory[count] = instruction[16:]
            count += 1

    def writeToMemory(self, value, index=None):  # Value is expected to be a decimal
        CHUNK_SIZE = 8
        a = format(value, "08b")
        b = "0" * (CHUNK_SIZE - len(a) % CHUNK_SIZE) + a
        for i in range(len(b) / CHUNK_SIZE):
            # TODO check for stackoverflow
            if(index):
                self.memory[index] = b[i*CHUNK_SIZE:(i+1)*CHUNK_SIZE]
                index -= 1
            else:
                self.memory[self.registers['S']
                            ] = b[i*CHUNK_SIZE:(i+1)*CHUNK_SIZE]
                self.registers['S'] -= 1

    def readFromMemory(self, index):
        return int(self.memory[index] + self.memory[index-1], 2)

    def popFromStack(self) -> int:
        r = ""
        for i in range(2):
            r += self.memory[self.registers['S']]
            self.memory[self.registers['S']] = None
            self.registers['S'] -= 1
        return int(r,2)

    def updateFlags(self, value: int, SF=False, ZF=False, CF=False):
        result = bin(value)[2:]
        if(CF and len(result) > 16):
            self.flags['CF'] = True
            result = result[-16]
        else:
            self.flags['CF'] = False
        if SF:
            self.flags['SF'] = result[0] == '1'
        if ZF:
            self.flags['ZF'] = int(result, 2) == 0
        return result

    def run(self):
        while True:
            # 24 bits string
            self.flags['JF'] = False
            currentInstruction = self.memory[self.registers["PC"]] + \
                self.memory[self.registers["PC"] + 1] + \
                self.memory[self.registers["PC"] + 2]
            instructionDetails = functions.GNUToBinary(currentInstruction)
            selectedFunction, address_mode, operand = instructionDetails
            a = functions.functionCodes[selectedFunction](
                self, address_mode, operand)
            if a:
                print("HALT!")
                break
            if not self.flags['JF']:
                self.registers['PC'] += 3
