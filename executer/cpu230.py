# import functions
import constants


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
        for i in range(len(b) // CHUNK_SIZE):
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
        poppedaddress = self.registers['S'] + 2
        for i in range(2):
            r += self.memory[ poppedaddress]
            self.memory[self.registers['S']] = None
            poppedaddress-=1
        self.registers['S']+=2
        return int(r, 2)

    def updateFlags(self, value: int, SF=False, ZF=False, CF=False):
        result = bin(value)[2:]
        if(CF and len(result) > 16):
            self.flags['CF'] = Truef
            result = result[-16]
        else:
            self.flags['CF'] = False
        if SF:
            self.flags['SF'] = result[0] == '1'
        if ZF:
            self.flags['ZF'] = int(result, 2) == 0
        return int(result, 2)

    def run(self):
        while True:
            # 24 bits string
            self.flags['JF'] = False
            currentInstruction = self.memory[self.registers["PC"]] + \
                self.memory[self.registers["PC"] + 1] + \
                self.memory[self.registers["PC"] + 2]
            instructionDetails = GNUToBinary(currentInstruction)
            selectedFunction, address_mode, operand = instructionDetails
            a = functionCodes[selectedFunction](
                self, address_mode, operand)
            if a:
                # print("HALT!")
                break
            if not self.flags['JF']:
                self.registers['PC'] += 3


def GNUToBinary(GNU):
    opcode = hex(int(GNU[0:6], 2))[2:].upper()
    addressing_mode = int(GNU[6:8], 2)
    operand = hex(int(GNU[8:], 2))[2:].upper()
    return opcode, addressing_mode, operand


def getValue(cpu: Cpu230, address_mode, operand):
    if address_mode == 0:  # Immediate data
        return int(operand, 16)
    if address_mode == 1:  # Register
        registerName = constants.registersCodes[operand]
        return cpu.registers[registerName]
    if address_mode == 2:  # [A]
        registerName = constants.registersCodes[operand]
        return cpu.readFromMemory(cpu.registers[registerName])
    if address_mode == 3:  # [00]
        # return cpu.memory[int(operand)]
        return cpu.readFromMemory(int(operand))


def setValue(cpu: Cpu230, address_mode, operand, value: int):
    if address_mode == 1:  # Register
        registerName = constants.registersCodes[operand]
        cpu.registers[registerName] = value
        return
    if address_mode == 2:
        registerName = constants.registersCodes[operand]
        cpu.writeToMemory(value, cpu.registers[registerName])
        return
    if address_mode == 3:
        cpu.writeToMemory(value, int(operand))
        return
    print("Sorun var write to memoryde")


def HALT(cpu, address_mode, operand, **kwargs):
    return True


def LOAD(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = value


def STORE(cpu:Cpu230, address_mode, operand, **kwargs):
    # print("STORE Function")

    if address_mode == 1:  # B
        registerName = constants.registersCodes[operand]
        cpu.registers[registerName] = cpu.registers['A']
        return
    if address_mode == 2:
        registerName = constants.registersCodes[operand]
        cpu.writeToMemory(value=cpu.registers['A'],index=cpu.registers[registerName])
        # cpu.memory[cpu.registers[registerName]] = cpu.registers['A']
        return
    print("I knew you were trouble when you walked in")
    return False
    

def ADD(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = cpu.updateFlags(value+regA)
    cpu.registers['A'] = result


def SUB(cpu: Cpu230, address_mode, operand, **kwargs):
    # What about immediate data
    value = getValue(cpu, address_mode, operand)
    inverseB = inverseBits(value)
    inverse = int(inverseB,2) + 1

    ADD(cpu, 0, hex(inverse)[2:])
    # result = bin(regA + value)[2:]


def INC(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    result = value + 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def DEC(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    result = value - 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def XOR(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value ^ regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def AND(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value & regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def OR(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value | regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def NOT(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    complBit = int(inverseBits(value),2)
    cpu.flags['ZF'] = compl == 0
    cpu.flags['SF'] = bin(compl)[3] == '1'
    setValue(cpu, address_mode, operand,compl)


def SHL(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    result = value << 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def SHR(cpu, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    result = value >> 1
    result = cpu.updateFlags(result, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def NOP(cpu, address_mode, operand, **kwargs):
    pass


def PUSH(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    cpu.writeToMemory(value)


def POP(cpu: Cpu230, address_mode, operand, **kwargs):
    popped = cpu.popFromStack()
    setValue(cpu, address_mode, operand, popped)


def CMP(cpu: Cpu230, address_mode, operand, **kwargs):
    regABackup = cpu.registers['A']
    SUB(cpu, address_mode, operand)
    cpu.registers['A'] = regABackup


def JMP(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['PC'] = value
    cpu.flags['JF'] = True


def JZ(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JNZ(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JC(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JNC(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JA(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((cpu.flags['SF'] and cpu.flags['CF'])):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JAE(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((cpu.flags['SF'] and cpu.flags['CF']) or cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JB(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((not cpu.flags['SF'] and not cpu.flags['CF'])):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def JBE(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((not cpu.flags['SF'] and not cpu.flags['CF']) or cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True


def READ(cpu: Cpu230, address_mode, operand, **kwargs):
    given = ord(input())  # int
    setValue(cpu, address_mode, operand, given)


def PRINT(cpu: Cpu230, address_mode, operand, **kwargs):
    value = getValue(cpu, address_mode, operand)
    print(chr(value), end=f"\t\tFor the  decimal ascii {value}\n")


def inverseBits(givenNum: int) -> str:
    return "".join([ '1' if x == '0' else '0' for x in format(givenNum,'08b')])


functionCodes = {}
functionCodes['1'] = HALT
functionCodes['2'] = LOAD
functionCodes['3'] = STORE
functionCodes['4'] = ADD
functionCodes['5'] = SUB
functionCodes['6'] = INC
functionCodes['7'] = DEC
functionCodes['8'] = XOR
functionCodes['9'] = AND
functionCodes['A'] = OR
functionCodes['B'] = NOT
functionCodes['C'] = SHL
functionCodes['D'] = SHR
functionCodes['E'] = NOP
functionCodes['F'] = PUSH
functionCodes['10'] = POP
functionCodes['11'] = CMP
functionCodes['12'] = JMP
functionCodes['13'] = JZ
functionCodes['14'] = JNZ
functionCodes['15'] = JC
functionCodes['16'] = JNC
functionCodes['17'] = JA
functionCodes['18'] = JAE
functionCodes['19'] = JB
functionCodes['1A'] = JBE
functionCodes['1B'] = READ
functionCodes['1C'] = PRINT
