import argparse
from pathlib import Path
from os import listdir
from os.path import isfile, join
from Parser import Parser
from CodeWriter import CodeWriter


def parse_arguments():
    parser = argparse.ArgumentParser(description='Name of the input VM \
                                     file or directory')
    parser.add_argument('--source', action='store', required=True,
                        dest='input_file', help='a source IR file for the \
                                                          virtual machine')

    args = parser.parse_args()
    return args.input_file


def validate(input_file):
    '''
    Validates input vm file
    '''
    input_str = Path(input_file)
    if input_str.is_file():
        if input_file.endswith('.vm'):
            return True
        else:
            print("Source file is not a valid .vm file")
    elif input_str.is_dir():
        files = get_files_from_directory(input_str)
        for file in files:
            if file.endswith('.vm'):
                return True
        print('Directory does not contain any .vm files')
    else:
        print(f"File {input_file} does not exists")
    return False


def get_files_from_directory(path):
    '''
    Returns a list containing only .vm files from directory
    '''
    files = [f for f in listdir(path) if isfile(
        join(path, f)) and f.endswith('.vm')]
    return files


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


def handle_file_output(line, code_writer):
    line = remove_comments(line)
    if line.strip():
        parser = Parser(line)
        parser.parse()
        if parser.command_type == 'C_PUSH' or \
                parser.command_type == 'C_POP':
            code_writer.write_push_pop(parser)
        elif parser.command_type == 'C_ARITHMETIC':
            code_writer.write_arithmetic(parser)
        elif parser.command_type == 'C_LABEL':
            code_writer.write_label(parser)
        elif parser.command_type == 'C_GOTO':
            code_writer.write_goto(parser)
        elif parser.command_type == 'C_IF':
            code_writer.write_if(parser)
        elif parser.command_type == 'C_FUNCTION':
            code_writer.write_function(parser)


def main():
    input_file = parse_arguments()
    if validate(input_file):
        if Path(input_file).is_dir():
            files = get_files_from_directory(input_file)
            code_writer = CodeWriter(input_file)
            for file in files:
                lines = read_file(f'{input_file}/{file}')
                for line in lines:
                    handle_file_output(line, code_writer)
        else:
            lines = read_file(input_file)
            code_writer = CodeWriter(input_file)
            for line in lines:
                handle_file_output(line, code_writer)


if __name__ == "__main__":
    main()
