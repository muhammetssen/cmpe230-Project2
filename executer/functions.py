import constants

def GNUToBinary(GNU):
    opcode = hex(int(GNU[0:6], 2))[2:].upper()
    addressing_mode = int(GNU[6:8], 2)
    operand = hex(int(GNU[8:], 2))[2:].upper()
    return opcode, addressing_mode, operand

def getValue(cpu, address_mode, operand):
    if address_mode == 0: ## Immediate data
        return int(operand,16)
    if address_mode == 1: ## Register
        registerName = constants.registersCodes[operand]
        return cpu.registers[registerName]
    if address_mode == 2: ## [A]
        registerName = constants.registersCodes[operand]
        return cpu.readFromMemory(cpu.registers[registerName])
    if address_mode == 3: ## [00]
        # return cpu.memory[int(operand)]
        return cpu.readFromMemory(int(operand))
    

def HALT(cpu, address_mode, operand, **kwargs):
    print("HALT Function")


def LOAD(cpu, address_mode, operand, **kwargs):
    print("LOAD Function")

    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = value
    

def STORE(cpu, address_mode, operand, **kwargs):
    print("STORE Function")
    
    if address_mode == 1: ## B
        registerName = constants.registersCodes[operand]
        cpu.registers[registerName] = cpu.registers['A']
        return
    if address_mode == 2:
        registerName = constants.registersCodes[operand]
        cpu.memory[cpu.registers[registerName]] = cpu.registers['A']
        return
    return False


def ADD(cpu, address_mode, operand, **kwargs):
    print("ADD Function")


def SUB(cpu, address_mode, operand, **kwargs):
    print("SUB Function")


def INC(cpu, address_mode, operand, **kwargs):
    print("INC Function")


def DEC(cpu, address_mode, operand, **kwargs):
    print("DEC Function")


def XOR(cpu, address_mode, operand, **kwargs):
    print("XOR Function")


def AND(cpu, address_mode, operand, **kwargs):
    print("AND Function")


def OR(cpu, address_mode, operand, **kwargs):
    print("OR Function")


def NOT(cpu, address_mode, operand, **kwargs):
    print("NOT Function")


def SHL(cpu, address_mode, operand, **kwargs):
    print("SHL Function")


def SHR(cpu, address_mode, operand, **kwargs):
    print("SHR Function")


def NOP(cpu, address_mode, operand, **kwargs):
    print("NOP Function")


def PUSH(cpu, address_mode, operand, **kwargs):
    print("PUSH Function")


def POP(cpu, address_mode, operand, **kwargs):
    print("POP Function")


def CMP(cpu, address_mode, operand, **kwargs):
    print("CMP Function")


def JMP(cpu, address_mode, operand, **kwargs):
    print("JMP Function")


def JZ(cpu, address_mode, operand, **kwargs):
    print("JZ Function")


def JE(cpu, address_mode, operand, **kwargs):
    print("JE Function")


def JNZ(cpu, address_mode, operand, **kwargs):
    print("JNZ Function")


def JNE(cpu, address_mode, operand, **kwargs):
    print("JNE Function")


def JC(cpu, address_mode, operand, **kwargs):
    print("JC Function")


def JNC(cpu, address_mode, operand, **kwargs):
    print("JNC Function")


def JA(cpu, address_mode, operand, **kwargs):
    print("JA Function")


def JAE(cpu, address_mode, operand, **kwargs):
    print("JAE Function")


def JB(cpu, address_mode, operand, **kwargs):
    print("JB Function")


def JBE(cpu, address_mode, operand, **kwargs):
    print("JBE Function")


def READ(cpu, address_mode, operand, **kwargs):
    print("READ Function")


def PRINT(cpu, address_mode, operand, **kwargs):
    print("PRINT Function")


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
functionCodes['13'] = JE
functionCodes['14'] = JNZ
functionCodes['14'] = JNE
functionCodes['15'] = JC
functionCodes['16'] = JNC
functionCodes['17'] = JA
functionCodes['18'] = JAE
functionCodes['19'] = JB
functionCodes['1A'] = JBE
functionCodes['1B'] = READ
functionCodes['1C'] = PRINT
