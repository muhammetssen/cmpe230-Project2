LOAD 7cd4
STORE B
LOAD 9b1f
STORE C
LOAD 0c594
STORE D
LOAD 706a
STORE E

        PRINT " "
        PRINT "0"
ADD 0e5de
        JMP TEST0
        LABEL0:


        PRINT " "
        PRINT "1"
ADD 0e5de
        JMP TEST1
        LABEL1:


        PRINT " "
        PRINT "2"
ADD 0e5de
        JMP TEST2
        LABEL2:


        PRINT " "
        PRINT "3"
ADD 0e5de
        JMP TEST3
        LABEL3:


        PRINT " "
        PRINT "4"
ADD 0e5de
        JMP TEST4
        LABEL4:


        PRINT " "
        PRINT "5"
ADD 0e5de
        JMP TEST5
        LABEL5:


        PRINT " "
        PRINT "6"
ADD 0e5de
        JMP TEST6
        LABEL6:


        PRINT " "
        PRINT "7"
ADD 0e5de
        JMP TEST7
        LABEL7:


        PRINT " "
        PRINT "8"
AND 53f8
        JMP TEST8
        LABEL8:


        PRINT " "
        PRINT "9"
AND 53f8
        JMP TEST9
        LABEL9:


        PRINT " "
        PRINT "0"
AND 53f8
        JMP TEST10
        LABEL10:


        PRINT " "
        PRINT "1"
AND 53f8
        JMP TEST11
        LABEL11:


        PRINT " "
        PRINT "2"
AND 53f8
        JMP TEST12
        LABEL12:


        PRINT " "
        PRINT "3"
AND 53f8
        JMP TEST13
        LABEL13:

        LOAD A
        CMP 80
        JBE PRINT0
PRINT A
        PRINT0:

        LOAD A
        CMP 80
        JBE PRINT1
PRINT A
        PRINT1:


        PRINT " "
        PRINT "4"
SUB 3049
        JMP TEST14
        LABEL14:


        PRINT " "
        PRINT "5"
SUB 3049
        JMP TEST15
        LABEL15:

LOAD C
        LOAD D
        CMP 80
        JBE PRINT2
PRINT A
        PRINT2:

LOAD B

        PRINT " "
        PRINT "6"
SHR A
        JMP TEST16
        LABEL16:


        PRINT " "
        PRINT "7"
SHL E
        JMP TEST17
        LABEL17:


        PRINT " "
        PRINT "8"
SHL E
        JMP TEST18
        LABEL18:


        PRINT " "
        PRINT "9"
SHL E
        JMP TEST19
        LABEL19:


        PRINT " "
        PRINT "0"
SHL E
        JMP TEST20
        LABEL20:

        LOAD B
        CMP 80
        JBE PRINT3
PRINT A
        PRINT3:


        PRINT " "
        PRINT "1"
AND 0c47a
        JMP TEST21
        LABEL21:


        PRINT " "
        PRINT "2"
AND 0c47a
        JMP TEST22
        LABEL22:


        PRINT " "
        PRINT "3"
AND 0c47a
        JMP TEST23
        LABEL23:


        PRINT " "
        PRINT "4"
AND 0c47a
        JMP TEST24
        LABEL24:


        PRINT " "
        PRINT "5"
AND 0c47a
        JMP TEST25
        LABEL25:


        PRINT " "
        PRINT "6"
AND 0c47a
        JMP TEST26
        LABEL26:


        PRINT " "
        PRINT "7"
AND 0c47a
        JMP TEST27
        LABEL27:


        PRINT " "
        PRINT "8"
AND 0c47a
        JMP TEST28
        LABEL28:


        PRINT " "
        PRINT "9"
AND 0c47a
        JMP TEST29
        LABEL29:

        LOAD C
        CMP 80
        JBE PRINT4
PRINT A
        PRINT4:

        LOAD A
        CMP 80
        JBE PRINT5
PRINT A
        PRINT5:


        PRINT " "
        PRINT "0"
DEC 55f0
        JMP TEST30
        LABEL30:


        PRINT " "
        PRINT "1"
DEC 55f0
        JMP TEST31
        LABEL31:


        PRINT " "
        PRINT "2"
DEC 55f0
        JMP TEST32
        LABEL32:


        PRINT " "
        PRINT "3"
DEC 55f0
        JMP TEST33
        LABEL33:


        PRINT " "
        PRINT "4"
DEC 55f0
        JMP TEST34
        LABEL34:


        PRINT " "
        PRINT "5"
DEC 55f0
        JMP TEST35
        LABEL35:


        PRINT " "
        PRINT "6"
DEC 55f0
        JMP TEST36
        LABEL36:


        PRINT " "
        PRINT "7"
XOR 9ee3
        JMP TEST37
        LABEL37:


        PRINT " "
        PRINT "8"
XOR 9ee3
        JMP TEST38
        LABEL38:


        PRINT " "
        PRINT "9"
XOR 9ee3
        JMP TEST39
        LABEL39:


        PRINT " "
        PRINT "0"
XOR 9ee3
        JMP TEST40
        LABEL40:


        PRINT " "
        PRINT "1"
XOR 9ee3
        JMP TEST41
        LABEL41:


        PRINT " "
        PRINT "2"
XOR 9ee3
        JMP TEST42
        LABEL42:


        PRINT " "
        PRINT "3"
XOR 9ee3
        JMP TEST43
        LABEL43:


        PRINT " "
        PRINT "4"
SHL B
        JMP TEST44
        LABEL44:


        PRINT " "
        PRINT "5"
SHL B
        JMP TEST45
        LABEL45:


        PRINT " "
        PRINT "6"
SHL B
        JMP TEST46
        LABEL46:


        PRINT " "
        PRINT "7"
SHL B
        JMP TEST47
        LABEL47:


        PRINT " "
        PRINT "8"
SHL B
        JMP TEST48
        LABEL48:


        PRINT " "
        PRINT "9"
SHL B
        JMP TEST49
        LABEL49:


        PRINT " "
        PRINT "0"
SHL B
        JMP TEST50
        LABEL50:


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

TEST11:
PRINT "#"
JZ JZ11
PRINT "a"
JZ11:
JE JE11
PRINT "b"
JE11:
JNZ JNZ11
PRINT "c"
JNZ11:
JNE JNE11
PRINT "d"
JNE11:
JC JC11
PRINT "e"
JC11:
JNC JNC11
PRINT "f"
JNC11:
JA JA11
PRINT "g"
JA11:
JAE JAE11
PRINT "h"
JAE11:
JB JB11
PRINT "i"
JB11:
JBE JBE11
PRINT "j"
JBE11:
PRINT "#"
JMP LABEL11

TEST12:
PRINT "#"
JZ JZ12
PRINT "a"
JZ12:
JE JE12
PRINT "b"
JE12:
JNZ JNZ12
PRINT "c"
JNZ12:
JNE JNE12
PRINT "d"
JNE12:
JC JC12
PRINT "e"
JC12:
JNC JNC12
PRINT "f"
JNC12:
JA JA12
PRINT "g"
JA12:
JAE JAE12
PRINT "h"
JAE12:
JB JB12
PRINT "i"
JB12:
JBE JBE12
PRINT "j"
JBE12:
PRINT "#"
JMP LABEL12

TEST13:
PRINT "#"
JZ JZ13
PRINT "a"
JZ13:
JE JE13
PRINT "b"
JE13:
JNZ JNZ13
PRINT "c"
JNZ13:
JNE JNE13
PRINT "d"
JNE13:
JC JC13
PRINT "e"
JC13:
JNC JNC13
PRINT "f"
JNC13:
JA JA13
PRINT "g"
JA13:
JAE JAE13
PRINT "h"
JAE13:
JB JB13
PRINT "i"
JB13:
JBE JBE13
PRINT "j"
JBE13:
PRINT "#"
JMP LABEL13

TEST14:
PRINT "#"
JZ JZ14
PRINT "a"
JZ14:
JE JE14
PRINT "b"
JE14:
JNZ JNZ14
PRINT "c"
JNZ14:
JNE JNE14
PRINT "d"
JNE14:
JC JC14
PRINT "e"
JC14:
JNC JNC14
PRINT "f"
JNC14:
JA JA14
PRINT "g"
JA14:
JAE JAE14
PRINT "h"
JAE14:
JB JB14
PRINT "i"
JB14:
JBE JBE14
PRINT "j"
JBE14:
PRINT "#"
JMP LABEL14

TEST15:
PRINT "#"
JZ JZ15
PRINT "a"
JZ15:
JE JE15
PRINT "b"
JE15:
JNZ JNZ15
PRINT "c"
JNZ15:
JNE JNE15
PRINT "d"
JNE15:
JC JC15
PRINT "e"
JC15:
JNC JNC15
PRINT "f"
JNC15:
JA JA15
PRINT "g"
JA15:
JAE JAE15
PRINT "h"
JAE15:
JB JB15
PRINT "i"
JB15:
JBE JBE15
PRINT "j"
JBE15:
PRINT "#"
JMP LABEL15

TEST16:
PRINT "#"
JZ JZ16
PRINT "a"
JZ16:
JE JE16
PRINT "b"
JE16:
JNZ JNZ16
PRINT "c"
JNZ16:
JNE JNE16
PRINT "d"
JNE16:
JC JC16
PRINT "e"
JC16:
JNC JNC16
PRINT "f"
JNC16:
JA JA16
PRINT "g"
JA16:
JAE JAE16
PRINT "h"
JAE16:
JB JB16
PRINT "i"
JB16:
JBE JBE16
PRINT "j"
JBE16:
PRINT "#"
JMP LABEL16

TEST17:
PRINT "#"
JZ JZ17
PRINT "a"
JZ17:
JE JE17
PRINT "b"
JE17:
JNZ JNZ17
PRINT "c"
JNZ17:
JNE JNE17
PRINT "d"
JNE17:
JC JC17
PRINT "e"
JC17:
JNC JNC17
PRINT "f"
JNC17:
JA JA17
PRINT "g"
JA17:
JAE JAE17
PRINT "h"
JAE17:
JB JB17
PRINT "i"
JB17:
JBE JBE17
PRINT "j"
JBE17:
PRINT "#"
JMP LABEL17

TEST18:
PRINT "#"
JZ JZ18
PRINT "a"
JZ18:
JE JE18
PRINT "b"
JE18:
JNZ JNZ18
PRINT "c"
JNZ18:
JNE JNE18
PRINT "d"
JNE18:
JC JC18
PRINT "e"
JC18:
JNC JNC18
PRINT "f"
JNC18:
JA JA18
PRINT "g"
JA18:
JAE JAE18
PRINT "h"
JAE18:
JB JB18
PRINT "i"
JB18:
JBE JBE18
PRINT "j"
JBE18:
PRINT "#"
JMP LABEL18

TEST19:
PRINT "#"
JZ JZ19
PRINT "a"
JZ19:
JE JE19
PRINT "b"
JE19:
JNZ JNZ19
PRINT "c"
JNZ19:
JNE JNE19
PRINT "d"
JNE19:
JC JC19
PRINT "e"
JC19:
JNC JNC19
PRINT "f"
JNC19:
JA JA19
PRINT "g"
JA19:
JAE JAE19
PRINT "h"
JAE19:
JB JB19
PRINT "i"
JB19:
JBE JBE19
PRINT "j"
JBE19:
PRINT "#"
JMP LABEL19

TEST20:
PRINT "#"
JZ JZ20
PRINT "a"
JZ20:
JE JE20
PRINT "b"
JE20:
JNZ JNZ20
PRINT "c"
JNZ20:
JNE JNE20
PRINT "d"
JNE20:
JC JC20
PRINT "e"
JC20:
JNC JNC20
PRINT "f"
JNC20:
JA JA20
PRINT "g"
JA20:
JAE JAE20
PRINT "h"
JAE20:
JB JB20
PRINT "i"
JB20:
JBE JBE20
PRINT "j"
JBE20:
PRINT "#"
JMP LABEL20

TEST21:
PRINT "#"
JZ JZ21
PRINT "a"
JZ21:
JE JE21
PRINT "b"
JE21:
JNZ JNZ21
PRINT "c"
JNZ21:
JNE JNE21
PRINT "d"
JNE21:
JC JC21
PRINT "e"
JC21:
JNC JNC21
PRINT "f"
JNC21:
JA JA21
PRINT "g"
JA21:
JAE JAE21
PRINT "h"
JAE21:
JB JB21
PRINT "i"
JB21:
JBE JBE21
PRINT "j"
JBE21:
PRINT "#"
JMP LABEL21

TEST22:
PRINT "#"
JZ JZ22
PRINT "a"
JZ22:
JE JE22
PRINT "b"
JE22:
JNZ JNZ22
PRINT "c"
JNZ22:
JNE JNE22
PRINT "d"
JNE22:
JC JC22
PRINT "e"
JC22:
JNC JNC22
PRINT "f"
JNC22:
JA JA22
PRINT "g"
JA22:
JAE JAE22
PRINT "h"
JAE22:
JB JB22
PRINT "i"
JB22:
JBE JBE22
PRINT "j"
JBE22:
PRINT "#"
JMP LABEL22

TEST23:
PRINT "#"
JZ JZ23
PRINT "a"
JZ23:
JE JE23
PRINT "b"
JE23:
JNZ JNZ23
PRINT "c"
JNZ23:
JNE JNE23
PRINT "d"
JNE23:
JC JC23
PRINT "e"
JC23:
JNC JNC23
PRINT "f"
JNC23:
JA JA23
PRINT "g"
JA23:
JAE JAE23
PRINT "h"
JAE23:
JB JB23
PRINT "i"
JB23:
JBE JBE23
PRINT "j"
JBE23:
PRINT "#"
JMP LABEL23

TEST24:
PRINT "#"
JZ JZ24
PRINT "a"
JZ24:
JE JE24
PRINT "b"
JE24:
JNZ JNZ24
PRINT "c"
JNZ24:
JNE JNE24
PRINT "d"
JNE24:
JC JC24
PRINT "e"
JC24:
JNC JNC24
PRINT "f"
JNC24:
JA JA24
PRINT "g"
JA24:
JAE JAE24
PRINT "h"
JAE24:
JB JB24
PRINT "i"
JB24:
JBE JBE24
PRINT "j"
JBE24:
PRINT "#"
JMP LABEL24

TEST25:
PRINT "#"
JZ JZ25
PRINT "a"
JZ25:
JE JE25
PRINT "b"
JE25:
JNZ JNZ25
PRINT "c"
JNZ25:
JNE JNE25
PRINT "d"
JNE25:
JC JC25
PRINT "e"
JC25:
JNC JNC25
PRINT "f"
JNC25:
JA JA25
PRINT "g"
JA25:
JAE JAE25
PRINT "h"
JAE25:
JB JB25
PRINT "i"
JB25:
JBE JBE25
PRINT "j"
JBE25:
PRINT "#"
JMP LABEL25

TEST26:
PRINT "#"
JZ JZ26
PRINT "a"
JZ26:
JE JE26
PRINT "b"
JE26:
JNZ JNZ26
PRINT "c"
JNZ26:
JNE JNE26
PRINT "d"
JNE26:
JC JC26
PRINT "e"
JC26:
JNC JNC26
PRINT "f"
JNC26:
JA JA26
PRINT "g"
JA26:
JAE JAE26
PRINT "h"
JAE26:
JB JB26
PRINT "i"
JB26:
JBE JBE26
PRINT "j"
JBE26:
PRINT "#"
JMP LABEL26

TEST27:
PRINT "#"
JZ JZ27
PRINT "a"
JZ27:
JE JE27
PRINT "b"
JE27:
JNZ JNZ27
PRINT "c"
JNZ27:
JNE JNE27
PRINT "d"
JNE27:
JC JC27
PRINT "e"
JC27:
JNC JNC27
PRINT "f"
JNC27:
JA JA27
PRINT "g"
JA27:
JAE JAE27
PRINT "h"
JAE27:
JB JB27
PRINT "i"
JB27:
JBE JBE27
PRINT "j"
JBE27:
PRINT "#"
JMP LABEL27

TEST28:
PRINT "#"
JZ JZ28
PRINT "a"
JZ28:
JE JE28
PRINT "b"
JE28:
JNZ JNZ28
PRINT "c"
JNZ28:
JNE JNE28
PRINT "d"
JNE28:
JC JC28
PRINT "e"
JC28:
JNC JNC28
PRINT "f"
JNC28:
JA JA28
PRINT "g"
JA28:
JAE JAE28
PRINT "h"
JAE28:
JB JB28
PRINT "i"
JB28:
JBE JBE28
PRINT "j"
JBE28:
PRINT "#"
JMP LABEL28

TEST29:
PRINT "#"
JZ JZ29
PRINT "a"
JZ29:
JE JE29
PRINT "b"
JE29:
JNZ JNZ29
PRINT "c"
JNZ29:
JNE JNE29
PRINT "d"
JNE29:
JC JC29
PRINT "e"
JC29:
JNC JNC29
PRINT "f"
JNC29:
JA JA29
PRINT "g"
JA29:
JAE JAE29
PRINT "h"
JAE29:
JB JB29
PRINT "i"
JB29:
JBE JBE29
PRINT "j"
JBE29:
PRINT "#"
JMP LABEL29

TEST30:
PRINT "#"
JZ JZ30
PRINT "a"
JZ30:
JE JE30
PRINT "b"
JE30:
JNZ JNZ30
PRINT "c"
JNZ30:
JNE JNE30
PRINT "d"
JNE30:
JC JC30
PRINT "e"
JC30:
JNC JNC30
PRINT "f"
JNC30:
JA JA30
PRINT "g"
JA30:
JAE JAE30
PRINT "h"
JAE30:
JB JB30
PRINT "i"
JB30:
JBE JBE30
PRINT "j"
JBE30:
PRINT "#"
JMP LABEL30

TEST31:
PRINT "#"
JZ JZ31
PRINT "a"
JZ31:
JE JE31
PRINT "b"
JE31:
JNZ JNZ31
PRINT "c"
JNZ31:
JNE JNE31
PRINT "d"
JNE31:
JC JC31
PRINT "e"
JC31:
JNC JNC31
PRINT "f"
JNC31:
JA JA31
PRINT "g"
JA31:
JAE JAE31
PRINT "h"
JAE31:
JB JB31
PRINT "i"
JB31:
JBE JBE31
PRINT "j"
JBE31:
PRINT "#"
JMP LABEL31

TEST32:
PRINT "#"
JZ JZ32
PRINT "a"
JZ32:
JE JE32
PRINT "b"
JE32:
JNZ JNZ32
PRINT "c"
JNZ32:
JNE JNE32
PRINT "d"
JNE32:
JC JC32
PRINT "e"
JC32:
JNC JNC32
PRINT "f"
JNC32:
JA JA32
PRINT "g"
JA32:
JAE JAE32
PRINT "h"
JAE32:
JB JB32
PRINT "i"
JB32:
JBE JBE32
PRINT "j"
JBE32:
PRINT "#"
JMP LABEL32

TEST33:
PRINT "#"
JZ JZ33
PRINT "a"
JZ33:
JE JE33
PRINT "b"
JE33:
JNZ JNZ33
PRINT "c"
JNZ33:
JNE JNE33
PRINT "d"
JNE33:
JC JC33
PRINT "e"
JC33:
JNC JNC33
PRINT "f"
JNC33:
JA JA33
PRINT "g"
JA33:
JAE JAE33
PRINT "h"
JAE33:
JB JB33
PRINT "i"
JB33:
JBE JBE33
PRINT "j"
JBE33:
PRINT "#"
JMP LABEL33

TEST34:
PRINT "#"
JZ JZ34
PRINT "a"
JZ34:
JE JE34
PRINT "b"
JE34:
JNZ JNZ34
PRINT "c"
JNZ34:
JNE JNE34
PRINT "d"
JNE34:
JC JC34
PRINT "e"
JC34:
JNC JNC34
PRINT "f"
JNC34:
JA JA34
PRINT "g"
JA34:
JAE JAE34
PRINT "h"
JAE34:
JB JB34
PRINT "i"
JB34:
JBE JBE34
PRINT "j"
JBE34:
PRINT "#"
JMP LABEL34

TEST35:
PRINT "#"
JZ JZ35
PRINT "a"
JZ35:
JE JE35
PRINT "b"
JE35:
JNZ JNZ35
PRINT "c"
JNZ35:
JNE JNE35
PRINT "d"
JNE35:
JC JC35
PRINT "e"
JC35:
JNC JNC35
PRINT "f"
JNC35:
JA JA35
PRINT "g"
JA35:
JAE JAE35
PRINT "h"
JAE35:
JB JB35
PRINT "i"
JB35:
JBE JBE35
PRINT "j"
JBE35:
PRINT "#"
JMP LABEL35

TEST36:
PRINT "#"
JZ JZ36
PRINT "a"
JZ36:
JE JE36
PRINT "b"
JE36:
JNZ JNZ36
PRINT "c"
JNZ36:
JNE JNE36
PRINT "d"
JNE36:
JC JC36
PRINT "e"
JC36:
JNC JNC36
PRINT "f"
JNC36:
JA JA36
PRINT "g"
JA36:
JAE JAE36
PRINT "h"
JAE36:
JB JB36
PRINT "i"
JB36:
JBE JBE36
PRINT "j"
JBE36:
PRINT "#"
JMP LABEL36

TEST37:
PRINT "#"
JZ JZ37
PRINT "a"
JZ37:
JE JE37
PRINT "b"
JE37:
JNZ JNZ37
PRINT "c"
JNZ37:
JNE JNE37
PRINT "d"
JNE37:
JC JC37
PRINT "e"
JC37:
JNC JNC37
PRINT "f"
JNC37:
JA JA37
PRINT "g"
JA37:
JAE JAE37
PRINT "h"
JAE37:
JB JB37
PRINT "i"
JB37:
JBE JBE37
PRINT "j"
JBE37:
PRINT "#"
JMP LABEL37

TEST38:
PRINT "#"
JZ JZ38
PRINT "a"
JZ38:
JE JE38
PRINT "b"
JE38:
JNZ JNZ38
PRINT "c"
JNZ38:
JNE JNE38
PRINT "d"
JNE38:
JC JC38
PRINT "e"
JC38:
JNC JNC38
PRINT "f"
JNC38:
JA JA38
PRINT "g"
JA38:
JAE JAE38
PRINT "h"
JAE38:
JB JB38
PRINT "i"
JB38:
JBE JBE38
PRINT "j"
JBE38:
PRINT "#"
JMP LABEL38

TEST39:
PRINT "#"
JZ JZ39
PRINT "a"
JZ39:
JE JE39
PRINT "b"
JE39:
JNZ JNZ39
PRINT "c"
JNZ39:
JNE JNE39
PRINT "d"
JNE39:
JC JC39
PRINT "e"
JC39:
JNC JNC39
PRINT "f"
JNC39:
JA JA39
PRINT "g"
JA39:
JAE JAE39
PRINT "h"
JAE39:
JB JB39
PRINT "i"
JB39:
JBE JBE39
PRINT "j"
JBE39:
PRINT "#"
JMP LABEL39

TEST40:
PRINT "#"
JZ JZ40
PRINT "a"
JZ40:
JE JE40
PRINT "b"
JE40:
JNZ JNZ40
PRINT "c"
JNZ40:
JNE JNE40
PRINT "d"
JNE40:
JC JC40
PRINT "e"
JC40:
JNC JNC40
PRINT "f"
JNC40:
JA JA40
PRINT "g"
JA40:
JAE JAE40
PRINT "h"
JAE40:
JB JB40
PRINT "i"
JB40:
JBE JBE40
PRINT "j"
JBE40:
PRINT "#"
JMP LABEL40

TEST41:
PRINT "#"
JZ JZ41
PRINT "a"
JZ41:
JE JE41
PRINT "b"
JE41:
JNZ JNZ41
PRINT "c"
JNZ41:
JNE JNE41
PRINT "d"
JNE41:
JC JC41
PRINT "e"
JC41:
JNC JNC41
PRINT "f"
JNC41:
JA JA41
PRINT "g"
JA41:
JAE JAE41
PRINT "h"
JAE41:
JB JB41
PRINT "i"
JB41:
JBE JBE41
PRINT "j"
JBE41:
PRINT "#"
JMP LABEL41

TEST42:
PRINT "#"
JZ JZ42
PRINT "a"
JZ42:
JE JE42
PRINT "b"
JE42:
JNZ JNZ42
PRINT "c"
JNZ42:
JNE JNE42
PRINT "d"
JNE42:
JC JC42
PRINT "e"
JC42:
JNC JNC42
PRINT "f"
JNC42:
JA JA42
PRINT "g"
JA42:
JAE JAE42
PRINT "h"
JAE42:
JB JB42
PRINT "i"
JB42:
JBE JBE42
PRINT "j"
JBE42:
PRINT "#"
JMP LABEL42

TEST43:
PRINT "#"
JZ JZ43
PRINT "a"
JZ43:
JE JE43
PRINT "b"
JE43:
JNZ JNZ43
PRINT "c"
JNZ43:
JNE JNE43
PRINT "d"
JNE43:
JC JC43
PRINT "e"
JC43:
JNC JNC43
PRINT "f"
JNC43:
JA JA43
PRINT "g"
JA43:
JAE JAE43
PRINT "h"
JAE43:
JB JB43
PRINT "i"
JB43:
JBE JBE43
PRINT "j"
JBE43:
PRINT "#"
JMP LABEL43

TEST44:
PRINT "#"
JZ JZ44
PRINT "a"
JZ44:
JE JE44
PRINT "b"
JE44:
JNZ JNZ44
PRINT "c"
JNZ44:
JNE JNE44
PRINT "d"
JNE44:
JC JC44
PRINT "e"
JC44:
JNC JNC44
PRINT "f"
JNC44:
JA JA44
PRINT "g"
JA44:
JAE JAE44
PRINT "h"
JAE44:
JB JB44
PRINT "i"
JB44:
JBE JBE44
PRINT "j"
JBE44:
PRINT "#"
JMP LABEL44

TEST45:
PRINT "#"
JZ JZ45
PRINT "a"
JZ45:
JE JE45
PRINT "b"
JE45:
JNZ JNZ45
PRINT "c"
JNZ45:
JNE JNE45
PRINT "d"
JNE45:
JC JC45
PRINT "e"
JC45:
JNC JNC45
PRINT "f"
JNC45:
JA JA45
PRINT "g"
JA45:
JAE JAE45
PRINT "h"
JAE45:
JB JB45
PRINT "i"
JB45:
JBE JBE45
PRINT "j"
JBE45:
PRINT "#"
JMP LABEL45

TEST46:
PRINT "#"
JZ JZ46
PRINT "a"
JZ46:
JE JE46
PRINT "b"
JE46:
JNZ JNZ46
PRINT "c"
JNZ46:
JNE JNE46
PRINT "d"
JNE46:
JC JC46
PRINT "e"
JC46:
JNC JNC46
PRINT "f"
JNC46:
JA JA46
PRINT "g"
JA46:
JAE JAE46
PRINT "h"
JAE46:
JB JB46
PRINT "i"
JB46:
JBE JBE46
PRINT "j"
JBE46:
PRINT "#"
JMP LABEL46

TEST47:
PRINT "#"
JZ JZ47
PRINT "a"
JZ47:
JE JE47
PRINT "b"
JE47:
JNZ JNZ47
PRINT "c"
JNZ47:
JNE JNE47
PRINT "d"
JNE47:
JC JC47
PRINT "e"
JC47:
JNC JNC47
PRINT "f"
JNC47:
JA JA47
PRINT "g"
JA47:
JAE JAE47
PRINT "h"
JAE47:
JB JB47
PRINT "i"
JB47:
JBE JBE47
PRINT "j"
JBE47:
PRINT "#"
JMP LABEL47

TEST48:
PRINT "#"
JZ JZ48
PRINT "a"
JZ48:
JE JE48
PRINT "b"
JE48:
JNZ JNZ48
PRINT "c"
JNZ48:
JNE JNE48
PRINT "d"
JNE48:
JC JC48
PRINT "e"
JC48:
JNC JNC48
PRINT "f"
JNC48:
JA JA48
PRINT "g"
JA48:
JAE JAE48
PRINT "h"
JAE48:
JB JB48
PRINT "i"
JB48:
JBE JBE48
PRINT "j"
JBE48:
PRINT "#"
JMP LABEL48

TEST49:
PRINT "#"
JZ JZ49
PRINT "a"
JZ49:
JE JE49
PRINT "b"
JE49:
JNZ JNZ49
PRINT "c"
JNZ49:
JNE JNE49
PRINT "d"
JNE49:
JC JC49
PRINT "e"
JC49:
JNC JNC49
PRINT "f"
JNC49:
JA JA49
PRINT "g"
JA49:
JAE JAE49
PRINT "h"
JAE49:
JB JB49
PRINT "i"
JB49:
JBE JBE49
PRINT "j"
JBE49:
PRINT "#"
JMP LABEL49

TEST50:
PRINT "#"
JZ JZ50
PRINT "a"
JZ50:
JE JE50
PRINT "b"
JE50:
JNZ JNZ50
PRINT "c"
JNZ50:
JNE JNE50
PRINT "d"
JNE50:
JC JC50
PRINT "e"
JC50:
JNC JNC50
PRINT "f"
JNC50:
JA JA50
PRINT "g"
JA50:
JAE JAE50
PRINT "h"
JAE50:
JB JB50
PRINT "i"
JB50:
JBE JBE50
PRINT "j"
JBE50:
PRINT "#"
JMP LABEL50
