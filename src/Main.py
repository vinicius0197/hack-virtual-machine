import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description='Name of the input VM file')
    parser.add_argument('--source', action='store', required=True,
                        dest='input_file', help='a source IR file for the \
                                                          virtual machine')

    args = parser.parse_args()
    return args.input_file


def validate(input):
    '''
    Validates input vm file
    '''
    file = Path(input)
    if file.is_file():
        if input.endswith('.vm'):
            return True
        else:
            print("Source file is not a valid .vm file")
    else:
        print(f"File {input} does not exists")
    return False


def main():
    input_file = parse_arguments()
    if validate(input_file):
        print('success')


if __name__ == "__main__":
    main()
