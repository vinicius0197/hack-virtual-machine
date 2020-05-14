import os


class CodeWriter:
    def __init__(self, output):
        self.file = self.__open_file(output)
        self.label_counter = 0

    def __open_file(self, output):
        output_file_name = os.path.splitext(os.path.normpath(
            output).split(os.path.sep)[-1])[0] + '.asm'
        f = open(output_file_name, 'w')
        return f

    def write_arithmetic(self, parser):
        if parser.command == 'add':
            out_comment = f'//add\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    A=M\n \
                    D=D+A\n \
                    @SP\n \
                    A=M\n \
                    A=A-1\n \
                    A=A-1\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
        elif parser.command == 'sub':
            out_comment = f'//sub\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    A=M\n \
                    D=A-D\n \
                    @SP\n \
                    A=M\n \
                    A=A-1\n \
                    A=A-1\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
        elif parser.command == 'neg':
            out_comment = f'//neg\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    D=-D\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
        elif parser.command == 'eq':
            out_comment = f'//eq\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    D=D-M\n \
                    @TRUE_{self.label_counter}\n \
                    D;JEQ\n \
                    @FALSE_{self.label_counter}\n \
                    D;JMP\n \
                    (TRUE_{self.label_counter})\n \
                    D=-1\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (FALSE_{self.label_counter})\n \
                    D=0\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (END_{self.label_counter})\n \
                    @SP\n \
                    A=M\n \
                    A=A-1\n \
                    A=A-1\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
            self.label_counter += 1
        elif parser.command == 'gt':
            out_comment = f'//gt\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    D=M-D\n \
                    @TRUE_{self.label_counter}\n \
                    D;JGT\n \
                    @FALSE_{self.label_counter}\n \
                    D;JMP\n \
                    (TRUE_{self.label_counter})\n \
                    D=-1\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (FALSE_{self.label_counter})\n \
                    D=0\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (END_{self.label_counter})\n \
                    @SP\n \
                    A=M\n \
                    A=A-1\n \
                    A=A-1\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
            self.label_counter += 1
        elif parser.command == 'lt':
            out_comment = f'//lt\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    D=M-D\n \
                    @TRUE_{self.label_counter}\n \
                    D;JLT\n \
                    @FALSE_{self.label_counter}\n \
                    D;JMP\n \
                    (TRUE_{self.label_counter})\n \
                    D=-1\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (FALSE_{self.label_counter})\n \
                    D=0\n \
                    @END_{self.label_counter}\n \
                    D;JMP\n \
                    (END_{self.label_counter})\n \
                    @SP\n \
                    A=M\n \
                    A=A-1\n \
                    A=A-1\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
            self.label_counter += 1
        elif parser.command == 'and':
            out_comment = f'//and\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    D=D&M\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
        elif parser.command == 'or':
            out_comment = f'//or\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=M\n \
                    A=A-1\n \
                    D=D|M\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)
        elif parser.command == 'not':
            out_comment = f'//not\n'
            out = f'@SP\n \
                    A=M\n \
                    A=A-1\n \
                    D=!M\n \
                    M=D\n \
                    D=A+1\n \
                    @SP\n \
                    M=D\n'.replace(" ", "")
            self.file.write(out_comment)
            self.file.write(out)

    def write_push_pop(self, parser):
        if parser.command_type == 'C_PUSH':
            segment = parser.segment
            index = parser.index
            if segment == 'constant':

                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@{index}\n \
                            D=A\n \
                            @SP\n \
                            A=M\n \
                            M=D\n \
                            @SP\n \
                            D=M\n \
                            D=D+1\n \
                            M=D\n'.replace(" ", "")
                    self.file.write(out_comment)
                    self.file.write(out)
                except ValueError:
                    raise Exception(
                        f'Invalid index "{index}" for \
                        {parser.command} instruction')
            elif segment == 'local':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@LCL\n \
                            D=M\n \
                            @{index}\n \
                            D=D+A\n \
                            A=D\n \
                            D=M\n \
                            @SP\n \
                            A=M\n \
                            M=D\n \
                            @SP\n \
                            D=M\n \
                            D=D+1\n \
                            M=D\n'.replace(" ", "")
                    self.file.write(out_comment)
                    self.file.write(out)
                except ValueError:
                    raise Exception(
                        f'Invalid index "{index}" for \
                        {parser.command} instruction')

        elif parser.command_type == 'C_POP':
            segment = parser.segment
            index = parser.index

            if segment == 'local':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            D=M-1\n \
                            M=D\n \
                            @LCL\n \
                            D=M\n \
                            @{index}\n \
                            D=D+A\n \
                            @R13\n \
                            M=D\n \
                            @SP\n \
                            A=M\n \
                            D=M\n \
                            @R13\n \
                            A=M\n \
                            M=D\n'.replace(" ", "")
                    self.file.write(out_comment)
                    self.file.write(out)
                except ValueError:
                    raise Exception(
                        f'Invalid index "{index}" for \
                        {parser.command} instruction')
