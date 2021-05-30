#
# USAGE
# python test.py <folder1> <folder2> ...
#

import sys
import os
import filecmp

arguments = sys.argv[1:]

if len(arguments) == 0:
    print("ERROR: Please provide the names of the testcase folders as argument")
    print("    Example: 'python test.py cases1'")
else:
    results = "\n## TEST RESULTS ##\n"
    total_results = {}

    for folder in arguments:
        results += "    FOLDER: %s\n" % folder
        nTest = 0
        nPassed = 0
        
        dir = "../%s/" % folder
        for source_file in os.listdir(dir + "assemblysource"):
            if source_file.endswith(".asm"):
                nTest += 1
                os.system("cp " + dir + "assemblysource/" + source_file + " input.asm")
                os.system("python single_file_test.py input")
                source_file = source_file[:-4]
                bin_res = filecmp.cmp(dir + "assembledprogram/" + source_file + ".bin", "input.bin")
                txt_res = filecmp.cmp(dir + "output/" + source_file + ".txt", "input.txt")

                passed = bin_res and txt_res
                if passed:
                    nPassed += 1
                results += "[1]" if passed else "[0]"
                results += " " + source_file
                if not passed:
                    results += " - Failed:"
                    if not bin_res:
                        results += " binary"
                    if not txt_res:
                        results += " txt-output"
                results += "\n"
        
        total_results[folder] = "%d/%d" % (nPassed,nTest)

    os.system("rm input.*")
    print(results)
    print("## SUMMARY ##")
    for key in total_results:
        print("%s - %s" % (total_results[key],key))
    