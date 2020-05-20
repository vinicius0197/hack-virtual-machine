import os
from pathlib import Path
from os.path import dirname, basename


class CodeWriter:
    def __init__(self, output):
        self.file = self.__open_file(output)
        self.label_counter = 0
        self.name = os.path.splitext(os.path.normpath(
            output).split(os.path.sep)[-1])[0]

    def __open_file(self, output):
        if Path(output).is_dir():
            output_file_name = basename(dirname(output)) + '.asm'
            file_path = f'{os.path.dirname(output)}/{output_file_name}'
            f = open(file_path, 'w')
        else:

            output_file_name = os.path.splitext(os.path.normpath(
                output).split(os.path.sep)[-1])[0] + '.asm'
            file_path = f'{os.path.dirname(output)}/{output_file_name}'
            f = open(file_path, 'w')
        return f

    def write_label(self, parser):
        out_comment = f'//label\n'
        out = f'({parser.label})\n'
        self.file.write(out_comment)
        self.file.write(out)

    def write_goto(self, parser):
        out_comment = f'//goto\n'
        out = f'@{parser.label}\n \
                0;JMP\n'.replace(" ", "")
        self.file.write(out_comment)
        self.file.write(out)

    def write_if(self, parser):
        out_comment = f'//if\n'
        out = f'@SP\n \
                M=M-1\n \
                A=M\n \
                D=M\n \
                @{parser.label}\n \
                D;JNE\n'.replace(" ", "")
        self.file.write(out_comment)
        self.file.write(out)

    def write_function(self, parser):
        out_comment = f'//function\n'
        out = f'({parser.function_name})\n \
                @{parser.variables}\n \
                D=A-1\n \
                (LOOP_{parser.function_name})\n \
                @SP\n \
                A=M\n \
                M=0\n \
                @SP\n \
                M=M+1\n \
                @LOOP_{parser.function_name}\n \
                D=D-1\n \
                D;JGE\n'.replace(" ", "")
        self.file.write(out_comment)
        self.file.write(out)

    def write_return(self, parser):
        out_comment = f'// return\n'
        out = f'// gets end frame\n \
                @LCL\n \
                D=M\n \
                @endFrame\n \
                M=D\n \
                // get return addr\n \
                @5\n \
                D=A\n \
                @endFrame\n \
                D=M-D\n \
                A=D\n \
                D=M\n \
                @retAddr\n \
                M=D\n \
                // pop return value from stack\n \
                @SP\n \
                M=M-1\n \
                A=M\n \
                D=M\n \
                // reposition the return value for the caller\n \
                @ARG\n \
                A=M\n \
                M=D\n \
                // reposition SP of the caller\n \
                @ARG\n \
                A=M\n \
                D=A+1\n \
                @SP\n \
                M=D\n \
                // restores THAT of the caller\n \
                @endFrame\n \
                D=M-1\n \
                A=D\n \
                D=M\n \
                @THAT\n \
                M=D\n \
                // restores THIS of the caller\n \
                @endFrame\n \
                D=M\n \
                @2\n \
                D=D-A\n \
                A=D\n \
                D=M\n \
                @THIS\n \
                M=D\n \
                // restores ARG of the caller\n \
                @endFrame\n \
                D=M\n \
                @3\n \
                D=D-A\n \
                A=D\n \
                D=M\n \
                @ARG\n \
                M=D\n \
                // restores LCL of the caller\n \
                @endFrame\n \
                D=M\n \
                @4\n \
                D=D-A\n \
                A=D\n \
                D=M\n \
                @LCL\n \
                M=D\n \
                // goes to return address\n \
                @retAddr\n \
                0;JMP\n'.replace(" ", "")
        self.file.write(out_comment)
        self.file.write(out)

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

            elif segment == 'this':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@THIS\n \
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

            elif segment == 'argument':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@ARG\n \
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

            elif segment == 'that':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@THAT\n \
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

            elif segment == 'temp':
                try:
                    int(index)
                    if int(index) > 7:
                        raise Exception(
                            f'Value {index} out of range for \
                              {parser.command} instruction')
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@5\n \
                            D=A\n \
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

            elif segment == 'pointer':
                try:
                    int(index)
                    if int(index) > 1 or int(index) < 0:
                        raise Exception(
                            f'Value {index} out of range for \
                              {parser.command} instruction. Must be 0 or 1')
                    out_comment = f'//{parser.command} {segment} {index}\n'

                    if int(index) == 0:
                        out = f'@THIS\n \
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

                    elif int(index) == 1:
                        out = f'@THAT\n \
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

            elif segment == 'static':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@{self.name}.{index}\n \
                            D=M\n \
                            @SP\n \
                            A=M\n \
                            M=D\n \
                            @SP\n \
                            M=M+1\n'.replace(" ", "")
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

            elif segment == 'argument':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            D=M-1\n \
                            M=D\n \
                            @ARG\n \
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

            elif segment == 'this':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            D=M-1\n \
                            M=D\n \
                            @THIS\n \
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

            elif segment == 'that':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            D=M-1\n \
                            M=D\n \
                            @THAT\n \
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

            elif segment == 'temp':
                try:
                    int(index)
                    if int(index) > 7:
                        raise Exception(
                            f'Value {index} out of range for \
                              {parser.command} instruction')
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            D=M-1\n \
                            M=D\n \
                            @5\n \
                            D=A\n \
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

            elif segment == 'pointer':
                try:
                    int(index)
                    if int(index) > 1 or int(index) < 0:
                        raise Exception(
                            f'Value {index} out of range for \
                              {parser.command} instruction. Must be 0 or 1')
                    out_comment = f'//{parser.command} {segment} {index}\n'

                    if int(index) == 0:
                        out = f'@SP\n \
                                D=M\n \
                                D=D-1\n \
                                M=D\n \
                                A=M\n \
                                D=M\n \
                                @THIS\n \
                                M=D\n'.replace(" ", "")
                        self.file.write(out_comment)
                        self.file.write(out)
                    elif int(index) == 1:
                        out = f'@SP\n \
                                D=M\n \
                                D=D-1\n \
                                M=D\n \
                                A=M\n \
                                D=M\n \
                                @THAT\n \
                                M=D\n'.replace(" ", "")
                        self.file.write(out_comment)
                        self.file.write(out)
                except ValueError:
                    raise Exception(
                        f'Invalid index "{index}" for \
                        {parser.command} instruction')

            elif segment == 'static':
                try:
                    int(index)
                    out_comment = f'//{parser.command} {segment} {index}\n'
                    out = f'@SP\n \
                            AM=M-1\n \
                            D=M\n \
                            @{self.name}.{index}\n \
                            M=D\n'.replace(" ", "")
                    self.file.write(out_comment)
                    self.file.write(out)
                except ValueError:
                    raise Exception(
                        f'Invalid index "{index}" for \
                        {parser.command} instruction')
