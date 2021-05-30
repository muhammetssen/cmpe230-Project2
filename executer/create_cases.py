
from random import choice, randint

jumps = ["JZ", "JE", "JNZ", "JNE", "JC", "JNC", "JA", "JAE", "JB", "JBE"]
possibleOperations = ["LOAD", "STORE", "ADD", "SUB", "DEC", "INC", "XOR", "AND", "OR", "NOT", "SHL", "SHR"] + ["PRINT"] * 5
possibleRegisters = ["A", "B", "C", "D", "E"]

def getHex():
    operand = hex(randint(0, 2**16 - 1))[2:]
    return formatHex(operand)

def formatHex(hex):
    return hex if hex[0].isnumeric() else "0"+hex

class TestWriter:

    def __init__(self):
        self.labelCounter = 0
        self.printCounter = 0

    def mountFile(self, f):
        self.file = open(f, "w")

    def dismountFile(self):
        self.file.write("\nHALT\n\n\n\n")
        for i in range(self.labelCounter):
            self.flagTest(i)
        self.file.close()

    def loadRandom(self):
        for register in possibleRegisters[1:]:
            self.file.write("LOAD %s\n" % getHex())
            self.file.write("STORE %s\n" % register)

    def flagTest(self, i):
        self.file.write("\nTEST" + str(i) + ":\n")
        self.file.write("PRINT \"#\"\n")
        for j,jump in enumerate(jumps):
            nextLabel = jump + str(i)
            self.file.write(jump + " " + nextLabel + "\n")
            self.file.write("PRINT \"" + chr(ord('a') + j) + "\"\n")
            self.file.write(nextLabel + ":\n")
        self.file.write("PRINT \"#\"\n")
        self.file.write("JMP " + "LABEL" + str(i) + "\n")

    def printGuard(self, operand):
        label = "PRINT%d" % self.printCounter
        self.file.write("        LOAD %s\n" % operand)
        self.file.write("        CMP 80\n") # 80 in hex is 128 in decimal
        self.file.write("        JBE %s\n" % label) # Jump if operand is above 128
        self.file.write("PRINT A\n")
        self.file.write("        %s:\n\n" % label)

        self.printCounter += 1

    def write(self, count, operation, operand, check=True):
        for i in range(count):
            if check:
                self.file.write("\n        PRINT \" \"\n")
                #self.file.write("        PRINT \"@\"\n")
                #self.file.write("        PRINT \" \"\n")
                self.file.write("        PRINT \"%d\"\n" % (self.labelCounter%10))
            self.file.write(operation + " " + operand + "\n")

            if check:
                self.file.write("        JMP TEST%d\n" % self.labelCounter)
                self.file.write("        LABEL%d:\n\n" % self.labelCounter)
                self.labelCounter += 1

# INC-DEC around 0000
def incDecCase(caseName):
    tw = TestWriter()
    tw.mountFile(caseName)
    tw.loadRandom()

    tw.write(2, "DEC", "A")
    tw.write(4, "INC", "A")
    tw.write(4, "DEC", "A")

    tw.dismountFile()

def caseRandom(nLines, caseName):
    tw = TestWriter()
    tw.mountFile(caseName)
    tw.loadRandom()

    lineCounter = 0
    while(lineCounter<nLines):
        operation = choice(possibleOperations)
        if operation in ["SHL", "SHR"]:
            operand = choice(possibleRegisters)
            n = randint(1, 10)
            tw.write(n, operation, operand)
            lineCounter += n
        elif operation in ["LOAD", "STORE"]:
            operand = choice(possibleRegisters[1:])
            tw.write(1, operation, operand, False)
            lineCounter += 1
            # TODO: add read/write to memory
        elif operation in ["PRINT"]:
            operand = choice(possibleRegisters)
            tw.printGuard(operand)
        else:
            roll = randint(0,5)
            n = randint(1, 10)
            if roll == 0: # use register
                operand = choice(possibleRegisters)
                tw.write(n, operation, operand)
            else: # use hexadecimal
                tw.write(n, operation, getHex())
            lineCounter += n

            
    tw.dismountFile()

def createCases(dir):

    incDecCase(dir + "/case1.asm")

    for i in range(2,10):
        caseRandom(10, "%s/case%d.asm" % (dir, i))
    for i in range(10, 20):
        caseRandom(50, "%s/case%d.asm" % (dir, i))
    for i in range(20, 30):
        caseRandom(100, "%s/case%d.asm" % (dir, i))

import sys
import os

def populateCases(dir):
    for source_file in os.listdir(dir + "/assemblysource"):
        source_file_address = dir + "/assemblysource/" + source_file
        os.system("cp %s input.asm" % source_file_address)
        os.system("python single_file_test.py input")
        os.system("mv input.bin %s%s.bin" % (dir + "/assembledprogram/", source_file[:-4]))
        os.system("mv input.txt %s%s.txt" % (dir + "/output/", source_file[:-4]))
        
dir = "../cases2"

#createCases(dir + "/assemblysource")
populateCases(dir)

# 04 - 06- infix- 10, all inclusive
# expect regular expression