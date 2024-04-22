from enum import Enum

class TokenType(Enum):
    INTEGER = 1
    FLOAT = 2
    OPERATOR = 3
    IDENTIFIER = 4
    # Add more token types as needed
import re

token_patterns = [
    (TokenType.INTEGER, r'\d+'),
    (TokenType.FLOAT, r'\d+\.\d+'),
    (TokenType.OPERATOR, r'[\+\-\*/]'),
    (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*')
]

def lex(input_string):
    tokens = []
    for pattern in token_patterns:
        token_type, regex = pattern
        for match in re.finditer(regex, input_string):
            tokens.append((token_type, match.group()))
    return tokens
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If value is equal, do nothing (assuming no duplicates)
def parse(tokens):
    ast = BinaryExpressionTree()
    for token_type, token_value in tokens:
        if token_type in [TokenType.INTEGER, TokenType.FLOAT, TokenType.IDENTIFIER]:
            ast.insert(token_value)
    return ast
def test():
    input_string = "3 + 4 * x - 2.5"
    print("Input string:", input_string)

    # Lexical analysis
    tokens = lex(input_string)
    print("Tokens:", tokens)

    # Parsing
    ast = parse(tokens)
    print("AST construction complete.")

test()
