//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//pop local 0
@SP
D=M-1
M=D
@LCL
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//label
(LOOP_START)
//push argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//push local 0
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//add
@SP
A=M
A=A-1
D=M
A=A-1
A=M
D=D+A
@SP
A=M
A=A-1
A=A-1
M=D
D=A+1
@SP
M=D
//pop local 0
@SP
D=M-1
M=D
@LCL
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//push argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//sub
@SP
A=M
A=A-1
D=M
A=A-1
A=M
D=A-D
@SP
A=M
A=A-1
A=A-1
M=D
D=A+1
@SP
M=D
//pop argument 0
@SP
D=M-1
M=D
@ARG
D=M
@0
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//push argument 0
@ARG
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//if
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE
//push local 0
@LCL
D=M
@0
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D