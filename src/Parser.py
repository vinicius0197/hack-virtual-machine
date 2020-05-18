class Parser:
    def __init__(self, line):
        self.line = line
        self.command = None
        self.segment = None
        self.index = None
        self.label = None

        self.command_type = None

    def parse(self):
        self.__tokenize()
        self.command_type = self.__get_command_type()

    def __tokenize(self):
        try:
            tokens = self.line.split()
            if self.command == 'function' or self.command == 'call':
                print('todo')
            else:
                self.command, self.segment, self.index = tokens
        except ValueError:
            try:
                tokens = self.line.split()
                self.command, self.label = tokens
            except ValueError:
                self.command = self.line.rstrip()
                self.segment = ''
                self.index = ''

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
        elif self.command == 'label':
            return 'C_LABEL'
        elif self.command == 'goto':
            return 'C_GOTO'
        elif self.command == 'if-goto':
            return 'C_IF'
        elif self.command == 'function':
            return 'C_FUNCTION'
        elif self.command == 'return':
            return 'C_RETURN'
        elif self.command == 'call':
            return 'C_CALL'
