import re

# Token types
IDENTIFIER = 'IDENTIFIER'
INTEGER = 'INTEGER'
CHAR = 'CHAR'
STRING = 'STRING'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
ASSIGN = 'ASSIGN'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EQUAL = 'EQUAL'
LESS = 'LESS'
GREATER = 'GREATER'
LESS_EQUAL = 'LESS_EQUAL'
GREATER_EQUAL = 'GREATER_EQUAL'
FOR = 'FOR'
IN = 'IN'
RANGE = 'RANGE'
IF = 'IF'
ELSE = 'ELSE'
PRINT= 'PRINT'
COLON = 'COLON'
INCREMENT = 'INCREMENT'
SPACE = 'SPACE'
NEWLINE = 'NEWLINE'
EOF = 'EOF'

# Regular expressions for token patterns
TOKEN_REGEX = [
    (r'[a-zA-Z][a-zA-Z0-9_]*', IDENTIFIER),
    (r'\d+', INTEGER),
    (r'\'[a-zA-Z\s][a-zA-Z\s]+\'', STRING),
    (r'\'[a-zA-Z]\'', CHAR),
    (r'\+=', INCREMENT),
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
    (r'==', EQUAL),
    (r'<=', LESS_EQUAL),
    (r'>=', GREATER_EQUAL),
    (r'<', LESS),
    (r'>', GREATER),
    (r'=', ASSIGN),
    (r':', COLON),
    (r'\s+', SPACE),
    (r'\n', NEWLINE)
]

KEY_WORDS = ['for', 'in', 'range', 'if', 'else', 'print', 'while' ]

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
        while self.pos < len(self.text):
            for pattern, token_type in TOKEN_REGEX:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    self.pos = match.end()
                    if token_type == SPACE or token_type == NEWLINE:
                        break  # Skip spaces
                    elif value in KEY_WORDS:
                        return Token(value.upper(), value)
                    else:
                        return Token(token_type, value)
            else:
                self.error()
        
        return Token(EOF, None)

if __name__ == '__main__':
    #lexer = Lexer("i = 5\n for i in range(10): print(i)\n i +=1\n if i == 10: print(Hello)\n else: print(World)")
    #lexer = Lexer("i = 0\n while i < 10: print(i)\n i += 1\n if i == 10: print(Hello)\n else: print(World)\n")
    lexer = Lexer("age = 18\n if age >= 18: print('You are an adult')\n else: print('You are a child')\n")
    while True:
        token = lexer.get_next_token()
        if token.type == EOF:
            break
        print(token)

