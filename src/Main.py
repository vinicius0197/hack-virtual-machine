import argparse
from pathlib import Path
from Parser import Parser
from CodeWriter import CodeWriter


def parse_arguments():
    parser = argparse.ArgumentParser(description='Name of the input VM file')
    parser.add_argument('--source', action='store', required=True,
                        dest='input_file', help='a source IR file for the \
                                                          virtual machine')

    args = parser.parse_args()
    return args.input_file


def validate(input_file):
    '''
    Validates input vm file
    '''
    file = Path(input_file)
    if file.is_file():
        if input_file.endswith('.vm'):
            return True
        else:
            print("Source file is not a valid .vm file")
    else:
        print(f"File {input_file} does not exists")
    return False


def read_file(input_file):
    '''
    Reads lines from the file
    '''
    f = open(input_file, "r")
    lines = f.readlines()
    return lines


def remove_comments(line):
    '''
    Remove comments from a line
    '''
    head, sep, tail = line.partition('//')
    return head


def main():
    input_file = parse_arguments()
    if validate(input_file):
        lines = read_file(input_file)
        code_writer = CodeWriter(input_file)
        for line in lines:
            line = remove_comments(line)
            if line.strip():
                parser = Parser(line)
                parser.parse()
                if parser.command_type == 'C_PUSH' or \
                   parser.command_type == 'C_POP':
                    code_writer.write_push_pop(parser)


if __name__ == "__main__":
    main()
