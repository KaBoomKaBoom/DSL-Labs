import re

# Token types
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
EOF = 'EOF'

# Regular expressions for token patterns
TOKEN_REGEX = [
    (r'\d+', INTEGER),
    (r'\+', PLUS),
    (r'-', MINUS),
    (r'\*', MULTIPLY),
    (r'/', DIVIDE),
    (r'\(', LPAREN),
    (r'\)', RPAREN),
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
        if self.pos >= len(self.text):
            return Token(EOF, None)

        text = self.text[self.pos:]

        for pattern, token_type in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(text)
            if match:
                value = match.group(0)
                self.pos += len(value)
                return Token(token_type, value)

        self.error()

if __name__ == '__main__':
    lexer = Lexer("3 + 5 * ( 10 - 2 ) / 4")
    while True:
        token = lexer.get_next_token()
        if token.type == EOF:
            break
        print(token)
