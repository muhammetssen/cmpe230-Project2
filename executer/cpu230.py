from re import A, findall


class Cpu230:
    flags = {
        "ZF": False,
        "CF": False,
        "SF": False,
        "JF": False  # We cannot increment PC after every instruction since it may jump to some other address. Hence, we are using this flag to be aware of jumps
    }
    # Registers hold integer decimal data
    registers = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "S": 64 * 1024 - 1,  # Stack starts from end of the memory
        "PC": 0  # Instruction to read
    }
    outputFilename: str

    memory = ['0' * 8] * 64 * 1024  # Memory is initialized with 0s.

    # Take a list of instructions, 24 bit strings, and write them to memory
    def instructionsToMemory(self, instructions):
        # Merge all the 24 bit insturctions to a string and split it to 8 bits sub strings
        chunks = findall(r".{8}", "".join(instructions))
        # Directly override the first part of the memory with the list of 8 bits string we just found
        self.memory[:len(chunks)] = chunks
    # Take an integer and write it to memory

    # Value is expected to be a decimal integer and index is an optinal parameter
    def writeToMemory(self, value: int, index=None):
        CHUNK_SIZE = 8  # Split the binary represantation of the value to 8 bit parts
        a = format(value, "08b")
        # Add zero(s) to start of the string if necessary
        b = "0" * (CHUNK_SIZE - len(a) % CHUNK_SIZE) + a
        for i in range(len(b) // CHUNK_SIZE):
            if(index):  # If an index was given as a parameter
                self.memory[index] = b[i * CHUNK_SIZE: (i+1) * CHUNK_SIZE]
                index -= 1
            else:
                self.memory[self.registers['S']
                            ] = b[i*CHUNK_SIZE:(i+1)*CHUNK_SIZE]
                self.registers['S'] -= 1
    # Get the value at the given index

    def readFromMemory(self, index) -> int:
        return int(self.memory[index] + self.memory[index-1], 2)

    # Pop data from the top of the stack
    def popFromStack(self) -> int:
        r = ""
        poppedaddress = self.registers['S'] + 2
        for i in range(2):
            r += self.memory[poppedaddress]
            self.memory[self.registers['S']] = '0' * 8
            poppedaddress -= 1
        self.registers['S'] += 2
        return int(r, 2)
    # Update the flags after an operation. Which flags to update can be chosed while calling the function

    def updateFlags(self, value: int, SF=False, ZF=False, CF=False) -> int:
        if SF:
            # If the value is positive or zero, sign flag is true
            self.flags['SF'] = value >= 0
        result = format(abs(value), '016b')
        if(CF and len(result) > 16):
            # If the result is 17 or more bits, carry flag is true
            self.flags['CF'] = True
            result = result[-16]
        else:
            self.flags['CF'] = False
        if ZF:
            # If the result is 0, Zero flag is true
            self.flags['ZF'] = int(result, 2) == 0
        return int(result, 2)

    def run(self):
        while True:
            self.flags['JF'] = False  # Reset the jump flag
            currentInstruction = self.memory[self.registers["PC"]] + \
                self.memory[self.registers["PC"] + 1] + \
                self.memory[self.registers["PC"] +
                            2]  # Get the next 24 bit instruction string from the memory
            selectedFunction, address_mode, operand = GNUToBinary(
                currentInstruction)  # Split the 24 bit instruction to 3 parts
            a = functionCodes[selectedFunction](  # Execute
                self, address_mode, operand)
            if a: # Functions return values runner need to be aware of like the program should continue or not
                break
            if not self.flags['JF']: # If there was not a jump in the execution, move to the next instruction
                self.registers['PC'] += 3


def GNUToBinary(GNU): #Split 24 bit instruction string to 3 parts
    opcode = hex(int(GNU[0:6], 2))[2:].upper()
    addressing_mode = int(GNU[6:8], 2)
    operand = hex(int(GNU[8:], 2))[2:].upper()
    return opcode, addressing_mode, operand

# Get the value by providing address mode and operand
def getValue(cpu: Cpu230, address_mode, operand) -> int:
    if address_mode == 0:  # Immediate data
        return int(operand, 16) # Convert hex to integer
    if address_mode == 1:  # Register
        registerName = registersCodes[int(operand)] # return register data
        return cpu.registers[registerName]
    if address_mode == 2:  # [A]
        registerName = registersCodes[int(operand)]
        return cpu.readFromMemory(cpu.registers[registerName]) # Return value from memory
    if address_mode == 3:  # [00]
        return cpu.readFromMemory(int(operand)) # Return value from memory

# Set the value by providing address mode, operand, and new value
# We don't use the return values from this function but having them is better for debug process
def setValue(cpu: Cpu230, address_mode, operand, value: int):
    # Beware that address mode cannot be 0 since modifying an immediate data is not feasible
    if address_mode == 1:  # Update Register
        registerName = registersCodes[int(operand)]
        cpu.registers[registerName] = value
        return True # We don't use this return 
    if address_mode == 2:
        registerName = registersCodes[int(operand)]
        cpu.writeToMemory(value, cpu.registers[registerName])
        return True
    if address_mode == 3:
        cpu.writeToMemory(value, int(operand))
        return True
    return False

# We dont care about parameters. Just return True so Cpu230.run function can exit
def HALT(_, __, ___):
    return True

# Get the value and store it in Register A
def LOAD(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = value

# Store the value in Reg a to given operand
def STORE(cpu: Cpu230, address_mode, operand):
    setValue(cpu,address_mode,operand,cpu.registers['A'])

# Add given operand with Reg A and set the flags accordingly and store the value in Reg A
def ADD(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    result = cpu.updateFlags(
        value+cpu.registers['A'], CF=True, SF=True, ZF=True)
    cpu.registers['A'] = result

# Subtract given operand from A and set the flags accordingly and store the value in Reg A
def SUB(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    res = findDif(cpu.registers['A'], value)
    result = cpu.updateFlags(res, CF=True, SF=True, ZF=True)
    cpu.registers['A'] = result

# Increment given operand by 1
def INC(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    result = cpu.updateFlags(value + 1, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)

# Decrement given operand by 1
def DEC(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    result = cpu.updateFlags(value - 1, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)

# XOR given operand by Reg A and store the value in Reg A
def XOR(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = cpu.updateFlags(
        value ^ cpu.registers['A'], SF=True, ZF=True)

# AND given operand by Reg A and store the value in Reg A
def AND(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = cpu.updateFlags(
        value & cpu.registers['A'], SF=True, ZF=True)

# OR given operand by Reg A and store the value in Reg A
def OR(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['A'] = cpu.updateFlags(
        value | cpu.registers['A'], SF=True, ZF=True)

# Take the inverse of bits of the given operand
def NOT(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    compl = int(inverseBits(value), 2)
    cpu.flags['ZF'] = compl == 0
    cpu.flags['SF'] = bin(compl)[3] == '1'
    setValue(cpu, address_mode, operand, compl)

# Shift bits in the given operand to 1 step left, hence multiply by 2
def SHL(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    result = cpu.updateFlags(value << 1, CF=True, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)

# Shift bits in the given operand to 1 step right, hence divide by 2
def SHR(cpu, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    result = cpu.updateFlags(value >> 1, SF=True, ZF=True)
    setValue(cpu, address_mode, operand, result)

# Do nothing
def NOP(_, __, ___):
    return

# Insert a new value to memory
def PUSH(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.writeToMemory(value)

# Get the last inserted value to memory
def POP(cpu: Cpu230, address_mode, operand):
    popped = cpu.popFromStack()
    setValue(cpu, address_mode, operand, popped)

# Compare the given operand and reg A
def CMP(cpu: Cpu230, address_mode, operand):
    regABackup = cpu.registers['A']
    SUB(cpu, address_mode, operand)
    cpu.registers['A'] = regABackup

# Jump to given line, without a condition
def JMP(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    cpu.registers['PC'] = value
    cpu.flags['JF'] = True

# Jump if last two compared numbers are equal or result of a arithmetic operation is 0
def JZ(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Inverse of JZ
def JNZ(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if carry flag is 1
def JC(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if(cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if carry flag is 0
def JNC(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if(not cpu.flags['CF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if Reg A is bigger than given operand
def JA(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if((cpu.flags['SF'] and not cpu.flags['ZF'])):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if Reg A is bigger than or equal to given operand
def JAE(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if((cpu.flags['SF']) or cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if Reg B is bigger than given operand
def JB(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if((not cpu.flags['SF'] and not cpu.flags['ZF'])):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Jump if Reg B is bigger than or equal to given operand
def JBE(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    if((not cpu.flags['SF']) or cpu.flags['ZF']):
        cpu.registers['PC'] = value
        cpu.flags['JF'] = True

# Read a character from the terminal and store it in the given operand
def READ(cpu: Cpu230, address_mode, operand):
    given = ord(input())  # int
    setValue(cpu, address_mode, operand, given)

# Print the wanted value to terminal
def PRINT(cpu: Cpu230, address_mode, operand):
    value = getValue(cpu, address_mode, operand)
    # print(chr(value))
    with open(cpu.outputFilename,"a") as f:
        f.write(chr(value)+"\n")

# Flip bits
def inverseBits(givenNum: int) -> str:
    return "".join(['1' if x == '0' else '0' for x in format(givenNum, '016b')])

# Find the difference of two integers, aka num1 - num2
def findDif(num1: int, num2: int) -> int:
    if num1 == 0:
        return -1 * num2
    if num2 == 0:
        return num1
    inversed = int(inverseBits(num2 - 1), 2)
    r = num1 + inversed
    trimmedBin = format(r, '016b')[-16:]
    trimmed = int(trimmedBin, 2)
    if(trimmedBin[0] == '1'):
        trimmed = -1 * int(inverseBits(trimmed - 1), 2)
    return trimmed


registersCodes = ["PC", "A", "B", "C", "D", "E", "S"]
functionCodes = {
    '1': HALT,
    '2': LOAD,
    '3': STORE,
    '4': ADD,
    '5': SUB,
    '6': INC,
    '7': DEC,
    '8': XOR,
    '9': AND,
    'A': OR,
    'B': NOT,
    'C': SHL,
    'D': SHR,
    'E': NOP,
    'F': PUSH,
    '10': POP,
    '11': CMP,
    '12': JMP,
    '13': JZ,
    '14': JNZ,
    '15': JC,
    '16': JNC,
    '17': JA,
    '18': JAE,
    '19': JB,
    '1A': JBE,
    '1B': READ,
    '1C': PRINT
}
