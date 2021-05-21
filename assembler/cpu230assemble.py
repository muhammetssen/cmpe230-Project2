from instructions import *

variables = {}

def calculateImmediate(operand):
    if "'" in operand:
        return hex(ord(operand[1:-1]))
    if operand in variables:
        return hex(variables[operand])
    return operand

outputs = []

file = open("prog.asm", "r")
inputLines = [line.strip() for line in file.readlines()]
file.close()

count = 0
for line in inputLines:
    if line[-1] == ":":
        variables[line[:-1]] = 3 * count
    else:
        count+=1

for line in inputLines:
    if line[-1] == ":":
        continue
    if line == "HALT":
        outputs.append("040000" + "\n")
        continue
    tokens = line.split()
    operator = tokens[0]
    codeType = codes[operator]
    address=tokens[1]
    addressType=getAddressType(address)

    if addressType == 0: #Immediate
       operand = calculateImmediate(address)
    elif addressType == 1: 
        operand = registers[address] # It is a register
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
    outputs.append(instr.upper() + "\n" )

outFile = open("out.bin","w")
outFile.writelines(outputs)
outFile.close()

