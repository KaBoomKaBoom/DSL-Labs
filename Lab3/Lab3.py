import re

# Token types
INTEGER = 'INTEGER'
CHAR = 'CHAR'
STRING = 'STRING'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
EQUAL = 'EQUAL'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
SPACE = 'SPACE'
EOF = 'EOF'

# Regular expressions for token patterns
TOKEN_REGEX = [
    (r'\d+', INTEGER),
    (r'[a-zA-Z][a-zA-Z]+', STRING),
    (r'[a-zA-Z]', CHAR),
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
    (r'=', EQUAL),
    (r'\s+', SPACE)
]

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception('Invalid character')

    def get_next_token(self):
        test = self.text.split(' ')
        if self.pos >= len(test):
            return Token(EOF, None)

        # for pattern, token_type in TOKEN_REGEX:
        #     regex = re.compile(pattern)
        #     match = regex.match(text)
        #     if match:
        #         value = match.group(0)
        #         self.pos += len(value)
        #         return Token(token_type, value)
        
        el = test[self.pos]
        print(el)
        for pattern, token_type in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(el)
            if match:
                self.pos += 1
                return Token(token_type, el)
            
            

        self.error()



if __name__ == '__main__':
    lexer = Lexer("te = 3 + 5 * ( 10 - 2 ) / 4")
    while True:
        token = lexer.get_next_token()
        if token.type == EOF:
            break
        print(token)
    lexer = "test = 3 + 5 * ( 10 - 2 ) / 4"
    #print(lexer.split(' '))