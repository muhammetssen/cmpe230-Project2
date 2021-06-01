import cpu230 
from sys import argv

if __name__== "__main__":
    # Create an instance of Cpu230 class
    myCpu = cpu230.Cpu230()
    f = open(argv[1],'r')
    lines = [format(int(line.strip(),16),'024b') for line in f.readlines()]
    f.close()
    myCpu.instructionsToMemory(lines) # Send instructions to memory
    myCpu.run() # Start running the instructions
    
    

    




