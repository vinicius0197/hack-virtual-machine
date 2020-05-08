class Parser:
    def __init__(self, line):
        self.line = line
        self.command = None
        self.segment = None
        self.index = None

        self.command_type = None

    def parse(self):
        self.__tokenize()
        self.command_type = self.__get_command_type()

    def __tokenize(self):
        tokens = self.line.split()
        self.command, self.segment, self.index = tokens

    def __get_command_type(self):
        if self.command == 'push':
            return 'C_PUSH'
        elif self.command == 'pop':
            return 'C_POP'
        elif self.command == 'add' or \
                self.command == 'sub' or \
                self.command == 'neg' or \
                self.command == 'eq' or \
                self.command == 'gt' or \
                self.command == 'lt' or \
                self.command == 'and' or  \
                self.command == 'or' or \
                self.command == 'not':
            return 'C_ARITHMETIC'
