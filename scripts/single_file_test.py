#
# USAGE:
#
# place the test case .asm file
# in the same directory with test.py
# Then call the script with 'python test.py <testcase> <flags>'
#
# Flags:
# -v: Verbose. Meaning that the program will print its status as it executes
#


import os
import sys

if len(sys.argv) == 1:
    print("ERROR: Please provide a file to run the test")
elif (sys.argv[1][-4:] == ".asm"):
    print("ERROR: If your file is case.asm, please call the test with 'python test.py case'")
else:
    case = sys.argv[1]
    willPrint = (len(sys.argv) == 3 and sys.argv[2] == "-v")
    if willPrint:
        print("### TEST STARTED ###")
        os.system("echo Running test on file " + case)

    os.system("python ../../cpu230assemble.py " + case + ".asm")

    if willPrint:
        print("### ASSEMBLING COMPLETED ###")

    os.system("python  ../../cpu230exec.py " + case + ".bin")

    if willPrint:
        print("### EXECUTION COMPLETED ###")
        print("### TEST COMPLETED ###")