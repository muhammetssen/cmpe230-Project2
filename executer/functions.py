from cpu230 import Cpu230
import constants


def GNUToBinary(GNU):
    opcode = hex(int(GNU[0:6], 2))[2:].upper()
    addressing_mode = int(GNU[6:8], 2)
    operand = hex(int(GNU[8:], 2))[2:].upper()
    return opcode, addressing_mode, operand


def getValue(cpu, address_mode, operand):
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
    print("HALT Function")

    return True

def LOAD(cpu, address_mode, operand, **kwargs):
    print("LOAD Function")

    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = value


def STORE(cpu, address_mode, operand, **kwargs):
    print("STORE Function")

    if address_mode == 1:  # B
        registerName = constants.registersCodes[operand]
        cpu.registers[registerName] = cpu.registers['A']
        return
    if address_mode == 2:
        registerName = constants.registersCodes[operand]
        cpu.memory[cpu.registers[registerName]] = cpu.registers['A']
        return
    return False


def ADD(cpu: Cpu230, address_mode, operand, **kwargs):
    print("ADD Function")

    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = bin(value + regA)[2:]
    if(len(result) > 16):
        cpu.flags['CF'] = True
        result = result[-16]
    else:
        cpu.flags['CF'] = False
    cpu.flags['SF'] = result[0] == '1'
    cpu.flags['ZF'] = int(result, 2) == 0

    cpu.registers['A'] = int(result, 2)


def SUB(cpu: Cpu230, address_mode, operand, **kwargs):
    print("SUB Function")
    # What about immediate data
    NOT(cpu, address_mode, operand)
    ADD(cpu, address_mode, operand)
    # value = getValue(cpu, address_mode, operand)
    # result = bin(regA + value)[2:]


def INC(cpu, address_mode, operand, **kwargs):
    print("INC Function")

    value = getValue(cpu, address_mode, operand)
    result = value + 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def DEC(cpu: Cpu230, address_mode, operand, **kwargs):
    print("DEC Function")

    value = getValue(cpu, address_mode, operand)
    result = value - 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def XOR(cpu: Cpu230, address_mode, operand, **kwargs):
    print("XOR Function")

    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value ^ regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def AND(cpu, address_mode, operand, **kwargs):
    print("AND Function")

    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value & regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def OR(cpu, address_mode, operand, **kwargs):
    print("OR Function")

    value = getValue(cpu, address_mode, operand)
    regA = cpu.registers['A']
    result = value | regA
    result = cpu.updateFlags(result, SF=True, ZF=True)
    cpu.registers['A'] = result


def NOT(cpu: Cpu230, address_mode, operand, **kwargs):
    print("NOT Function")

    value = getValue(cpu, address_mode, operand)
    compl = twosComplement(value)
    cpu.flags['ZF'] = compl == 0
    cpu.flags['SF'] = bin(compl)[3] == '1'


def SHL(cpu, address_mode, operand, **kwargs):
    print("SHL Function")

    value = getValue(cpu, address_mode, operand)
    result = value << 1
    result = cpu.updateFlags(result, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def SHR(cpu, address_mode, operand, **kwargs):
    print("SHR Function")

    value = getValue(cpu, address_mode, operand)
    result = value >> 1
    result = cpu.updateFlags(result, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)


def NOP(cpu, address_mode, operand, **kwargs):
    print("NOP Function")
    pass


def PUSH(cpu: Cpu230, address_mode, operand, **kwargs):
    print("PUSH Function")

    value = getValue(cpu, address_mode, operand)
    cpu.writeToMemory(value)


def POP(cpu: Cpu230, address_mode, operand, **kwargs):
    print("POP Function")

    popped = cpu.popFromStack()
    setValue(cpu, address_mode, operand, popped)


def CMP(cpu: Cpu230, address_mode, operand, **kwargs):
    print("CMP Function")

    regABackup = cpu.registers['A']
    SUB(cpu, address_mode, operand)
    cpu.registers['A'] = regABackup


def JMP(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JMP Function")

    value = getValue(cpu, address_mode, operand)
    cpu.registers['PC'] = value
    cpu.registers['JF'] = True


def JZ(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JZ Function")
    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JNZ(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JNZ Function")

    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JC(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JC Function")

    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JNC(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JNC Function")

    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JA(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JA Function")

    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((cpu.flags['SF'] and cpu.flags['CF'])):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JAE(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JAE Function")

    value = getValue(cpu, address_mode, operand)
    CMP(cpu, address_mode, operand)
    if((cpu.flags['SF'] and cpu.flags['CF']) or cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True


def JB(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JB Function")

    value = getValue(cpu, address_mode, operand)
    CMP(cpu,address_mode,operand)
    if((not cpu.flags['SF'] and not cpu.flags['CF'])):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True 

def JBE(cpu: Cpu230, address_mode, operand, **kwargs):
    print("JBE Function")

    value = getValue(cpu, address_mode, operand)
    CMP(cpu,address_mode,operand)
    if((not cpu.flags['SF'] and not cpu.flags['CF']) or cpu.flags['ZF'] ):
        cpu.registers['PC'] = value
        cpu.registers['JF'] = True 

def READ(cpu: Cpu230, address_mode, operand, **kwargs):
    print("READ Function")

    given = ord(input()) # int
    setValue(cpu,address_mode,operand,given)    


def PRINT(cpu: Cpu230, address_mode, operand, **kwargs):
    print("PRINT Function")
    value = getValue(cpu, address_mode, operand)
    print(chr(value))

def twosComplement(givenNum: int) -> int:
    return ~givenNum + 1


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
