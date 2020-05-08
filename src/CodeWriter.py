import os


class CodeWriter:
    def __init__(self, output):
        self.file = self.__open_file(output)

    def __open_file(self, output):
        output_file_name = os.path.splitext(os.path.normpath(
            output).split(os.path.sep)[-1])[0] + '.asm'
        f = open(output_file_name, 'w')
        return f

    def write_push_pop(self, parser):
        if parser.command_type == 'C_PUSH':
            segment = parser.segment
            index = parser.index

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
                    f'Invalid index "{index}" for {parser.command} instruction')
