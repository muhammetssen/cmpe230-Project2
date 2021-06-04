import cpu230 
from sys import argv

if __name__== "__main__":
    # Create an instance of Cpu230 class
    myCpu = cpu230.Cpu230()
    outfile = argv[1].split('.')[0] + ".txt"
    with open(outfile,"w") as f:
        f.close()  # Clear the file if it exists
    f = open(argv[1],'r')
    myCpu.outputFilename = outfile
    lines = [format(int(line.strip(),16),'024b') for line in f.readlines()]
    f.close()
    myCpu.instructionsToMemory(lines) # Send instructions to memory
    myCpu.run() # Start running the instructions
    
    

    




