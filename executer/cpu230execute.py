
from cpu230 import Cpu230





if __name__== "__main__":
    myCpu = Cpu230()
    f = open("prog.bin",'r')
    lines = [format(int(line.strip(),16),'024b') for line in f.readlines()]
    f.close()
    myCpu.instructionsToMemory(lines)
    myCpu.run()
    
    

    




