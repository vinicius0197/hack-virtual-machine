//push constant 10
@10
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
//push constant 21
@21
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//push constant 22
@22
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//pop argument 2
@SP
D=M-1
M=D
@ARG
D=M
@2
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//pop argument 1
@SP
D=M-1
M=D
@ARG
D=M
@1
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//push constant 36
@36
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//pop this 6
@SP
D=M-1
M=D
@THIS
D=M
@6
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//push constant 42
@42
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//push constant 45
@45
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//pop that 5
@SP
D=M-1
M=D
@THAT
D=M
@5
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//pop that 2
@SP
D=M-1
M=D
@THAT
D=M
@2
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
M=D
//push constant 510
@510
D=A
@SP
A=M
M=D
@SP
D=M
D=D+1
M=D
//pop temp 6
@SP
D=M-1
M=D
@5
D=A
@6
D=D+A
@R13
M=D
@SP
A=M
D=M
@R13
A=M
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
//push that 5
@THAT
D=M
@5
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
//push argument 1
@ARG
D=M
@1
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
//push this 6
@THIS
D=M
@6
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
//push this 6
@THIS
D=M
@6
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
//push temp 6
@5
D=A
@6
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