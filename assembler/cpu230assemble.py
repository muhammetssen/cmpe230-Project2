from instructions import *
from sys import argv
# We will store labels in this dict
labels = {}
# Find the value of immediate data by checking for quotes to identify ascii characters and labels
def calculateImmediate(operand):
    if "'" in operand:
        return hex(ord(operand[1:-1]))
    if operand in labels:
        return hex(labels[operand])
    return operand

outputs = [] # List of output binaries
givenFile = argv[1] 
outFile = givenFile.split('.')[0] + ".bin" 
file = open(givenFile, "r")
inputLines = [line.strip() for line in file.readlines() if line.strip() != '']
file.close()

count = 0 # Line counter. We did not increment this in label lines since they are not counted as an instruction.
for line in inputLines:
    if line[-1] == ":":
        labels[line[:-1]] = 3 * count # [:-1] means everything but the colon
    else:
        count+=1

for line in inputLines:
    if line[-1] == ":":
        continue
    if line == "HALT":
        outputs.append("040000")
        continue
    if line == "NOP":
        outputs.append("380000")
        continue
    
    tokens = line.split() # Split by whitespace
    operator = tokens[0] 
    codeType = codes[operator] # Instruction code of instruction
    address=tokens[1]
    addressType=getAddressType(address) # Get the address type by analyzing the operand

    if addressType == 0: #Immediate 
       operand = calculateImmediate(address)
    elif addressType == 1: # It is a register
        operand = registers[address] 
    elif addressType == 2: # [Memory Loc]
        operand = registers[address[1:-1]] # [A]
    else: # [Immediate]
        operand = calculateImmediate(address[1:-1])

    bopcode = format(int(codeType,16), '06b') 
    baddrmode = format(addressType, '02b') 
    boperand = format(int(operand,16), '016b') 
    binary =  bopcode + baddrmode + boperand 
    ibin = int(binary,2) 
    instr = format(ibin, '06x') 
    outputs.append(instr.upper())

outFile = open(outFile,"w")
outFile.write("\n".join(outputs))
outFile.close()

