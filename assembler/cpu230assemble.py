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
    elif addressType == 1: #Immediate
        if address in registers.keys():
            operand = registers[address] # It is a register
        else:
            operand = hex(variables[address]) # MYDATA
    elif addressType == 2: # [Memory Loc]
        inside = address[1:-1]
        if inside in registers.keys():
            operand = registers[inside] # [A]
        else:
            operand = hex(variables[inside]) # [MYDATA]
    else: # [Immediate]
        inside = address[1:-1]
        operand = calculateImmediate(inside)

    opcode   = codeType 
    addrmode = addressType
     
    # operand  = int(sys.argv[3],16) 

    bopcode = format(int(opcode,16), '06b') 
    baddrmode = format(addrmode, '02b') 
    boperand = format(int(operand,16), '016b') 
    bin = '0b' + bopcode + baddrmode + boperand 
    ibin = int(bin[2:],2) 
    instr = format(ibin, '06x') 
    outputs.append(instr.upper() + "\n" )

outFile = open("out.bin","w")
outFile.writelines(outputs)
outFile.close()

