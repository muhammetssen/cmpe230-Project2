LOAD 12df
STORE B
LOAD 92d2
STORE C
LOAD 2dc7
STORE D
LOAD 1f73
STORE E

        PRINT " "
        PRINT "0"
INC C
        JMP TEST0
        LABEL0:


        PRINT " "
        PRINT "1"
INC C
        JMP TEST1
        LABEL1:


        PRINT " "
        PRINT "2"
INC C
        JMP TEST2
        LABEL2:


        PRINT " "
        PRINT "3"
INC C
        JMP TEST3
        LABEL3:


        PRINT " "
        PRINT "4"
INC C
        JMP TEST4
        LABEL4:


        PRINT " "
        PRINT "5"
INC C
        JMP TEST5
        LABEL5:


        PRINT " "
        PRINT "6"
SUB E
        JMP TEST6
        LABEL6:


        PRINT " "
        PRINT "7"
SUB E
        JMP TEST7
        LABEL7:


        PRINT " "
        PRINT "8"
SUB E
        JMP TEST8
        LABEL8:


        PRINT " "
        PRINT "9"
SUB E
        JMP TEST9
        LABEL9:


        PRINT " "
        PRINT "0"
SUB E
        JMP TEST10
        LABEL10:


HALT




TEST0:
PRINT "#"
JZ JZ0
PRINT "a"
JZ0:
JE JE0
PRINT "b"
JE0:
JNZ JNZ0
PRINT "c"
JNZ0:
JNE JNE0
PRINT "d"
JNE0:
JC JC0
PRINT "e"
JC0:
JNC JNC0
PRINT "f"
JNC0:
JA JA0
PRINT "g"
JA0:
JAE JAE0
PRINT "h"
JAE0:
JB JB0
PRINT "i"
JB0:
JBE JBE0
PRINT "j"
JBE0:
PRINT "#"
JMP LABEL0

TEST1:
PRINT "#"
JZ JZ1
PRINT "a"
JZ1:
JE JE1
PRINT "b"
JE1:
JNZ JNZ1
PRINT "c"
JNZ1:
JNE JNE1
PRINT "d"
JNE1:
JC JC1
PRINT "e"
JC1:
JNC JNC1
PRINT "f"
JNC1:
JA JA1
PRINT "g"
JA1:
JAE JAE1
PRINT "h"
JAE1:
JB JB1
PRINT "i"
JB1:
JBE JBE1
PRINT "j"
JBE1:
PRINT "#"
JMP LABEL1

TEST2:
PRINT "#"
JZ JZ2
PRINT "a"
JZ2:
JE JE2
PRINT "b"
JE2:
JNZ JNZ2
PRINT "c"
JNZ2:
JNE JNE2
PRINT "d"
JNE2:
JC JC2
PRINT "e"
JC2:
JNC JNC2
PRINT "f"
JNC2:
JA JA2
PRINT "g"
JA2:
JAE JAE2
PRINT "h"
JAE2:
JB JB2
PRINT "i"
JB2:
JBE JBE2
PRINT "j"
JBE2:
PRINT "#"
JMP LABEL2

TEST3:
PRINT "#"
JZ JZ3
PRINT "a"
JZ3:
JE JE3
PRINT "b"
JE3:
JNZ JNZ3
PRINT "c"
JNZ3:
JNE JNE3
PRINT "d"
JNE3:
JC JC3
PRINT "e"
JC3:
JNC JNC3
PRINT "f"
JNC3:
JA JA3
PRINT "g"
JA3:
JAE JAE3
PRINT "h"
JAE3:
JB JB3
PRINT "i"
JB3:
JBE JBE3
PRINT "j"
JBE3:
PRINT "#"
JMP LABEL3

TEST4:
PRINT "#"
JZ JZ4
PRINT "a"
JZ4:
JE JE4
PRINT "b"
JE4:
JNZ JNZ4
PRINT "c"
JNZ4:
JNE JNE4
PRINT "d"
JNE4:
JC JC4
PRINT "e"
JC4:
JNC JNC4
PRINT "f"
JNC4:
JA JA4
PRINT "g"
JA4:
JAE JAE4
PRINT "h"
JAE4:
JB JB4
PRINT "i"
JB4:
JBE JBE4
PRINT "j"
JBE4:
PRINT "#"
JMP LABEL4

TEST5:
PRINT "#"
JZ JZ5
PRINT "a"
JZ5:
JE JE5
PRINT "b"
JE5:
JNZ JNZ5
PRINT "c"
JNZ5:
JNE JNE5
PRINT "d"
JNE5:
JC JC5
PRINT "e"
JC5:
JNC JNC5
PRINT "f"
JNC5:
JA JA5
PRINT "g"
JA5:
JAE JAE5
PRINT "h"
JAE5:
JB JB5
PRINT "i"
JB5:
JBE JBE5
PRINT "j"
JBE5:
PRINT "#"
JMP LABEL5

TEST6:
PRINT "#"
JZ JZ6
PRINT "a"
JZ6:
JE JE6
PRINT "b"
JE6:
JNZ JNZ6
PRINT "c"
JNZ6:
JNE JNE6
PRINT "d"
JNE6:
JC JC6
PRINT "e"
JC6:
JNC JNC6
PRINT "f"
JNC6:
JA JA6
PRINT "g"
JA6:
JAE JAE6
PRINT "h"
JAE6:
JB JB6
PRINT "i"
JB6:
JBE JBE6
PRINT "j"
JBE6:
PRINT "#"
JMP LABEL6

TEST7:
PRINT "#"
JZ JZ7
PRINT "a"
JZ7:
JE JE7
PRINT "b"
JE7:
JNZ JNZ7
PRINT "c"
JNZ7:
JNE JNE7
PRINT "d"
JNE7:
JC JC7
PRINT "e"
JC7:
JNC JNC7
PRINT "f"
JNC7:
JA JA7
PRINT "g"
JA7:
JAE JAE7
PRINT "h"
JAE7:
JB JB7
PRINT "i"
JB7:
JBE JBE7
PRINT "j"
JBE7:
PRINT "#"
JMP LABEL7

TEST8:
PRINT "#"
JZ JZ8
PRINT "a"
JZ8:
JE JE8
PRINT "b"
JE8:
JNZ JNZ8
PRINT "c"
JNZ8:
JNE JNE8
PRINT "d"
JNE8:
JC JC8
PRINT "e"
JC8:
JNC JNC8
PRINT "f"
JNC8:
JA JA8
PRINT "g"
JA8:
JAE JAE8
PRINT "h"
JAE8:
JB JB8
PRINT "i"
JB8:
JBE JBE8
PRINT "j"
JBE8:
PRINT "#"
JMP LABEL8

TEST9:
PRINT "#"
JZ JZ9
PRINT "a"
JZ9:
JE JE9
PRINT "b"
JE9:
JNZ JNZ9
PRINT "c"
JNZ9:
JNE JNE9
PRINT "d"
JNE9:
JC JC9
PRINT "e"
JC9:
JNC JNC9
PRINT "f"
JNC9:
JA JA9
PRINT "g"
JA9:
JAE JAE9
PRINT "h"
JAE9:
JB JB9
PRINT "i"
JB9:
JBE JBE9
PRINT "j"
JBE9:
PRINT "#"
JMP LABEL9

TEST10:
PRINT "#"
JZ JZ10
PRINT "a"
JZ10:
JE JE10
PRINT "b"
JE10:
JNZ JNZ10
PRINT "c"
JNZ10:
JNE JNE10
PRINT "d"
JNE10:
JC JC10
PRINT "e"
JC10:
JNC JNC10
PRINT "f"
JNC10:
JA JA10
PRINT "g"
JA10:
JAE JAE10
PRINT "h"
JAE10:
JB JB10
PRINT "i"
JB10:
JBE JBE10
PRINT "j"
JBE10:
PRINT "#"
JMP LABEL10