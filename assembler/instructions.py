codes = {
    "HALT":'1',
    "LOAD":'2',
    "STORE":'3',
    "ADD":'4',
    "SUB":'5',
    "INC":'6',
    "DEC":'7',
    "XOR":'8',
    "AND":'9',
    "OR":'A',
    "NOT":'B',
    "SHL":'C',
    "SHR":'D',
    "NOP":'E',
    "PUSH":'F',
    "POP":'10',
    "CMP":'11',
    "JMP":'12',
    "JZ":'13',
    "JE":'13',
    "JNZ":'14',
    "JNE":'14',
    "JC":'15',
    "JNC":'16',
    "JA":'17',
    "JAE":'18',
    "JB":'19',
    "JBE":'1A',
    "READ":'1B',
    "PRINT":'1C'
}
registers = {
    "PC":"0000",
    "A":"0001",
    "B":"0002",
    "C":"0003",
    "D":"0004",
    "E":"0005",
    "S":"0006"
}

def getAddressType(operandType):
    if '[' in operandType: # We are checking an address
        inside = operandType[1:-1]
        if "'" in inside:
            return 3
        if inside in registers.keys():
            return 2
        return 3
    if "'" in operandType:
        return 0
    if operandType in registers.keys():
        return 1
    return 0
      

