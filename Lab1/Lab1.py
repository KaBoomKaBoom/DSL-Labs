class Grammar:
    def __init__(self):
        self.S = 'S'
        self.V_n = ['S','D','R']
        self.V_t = ['a','b','c','d','f']
        self.P = {
            'S':['aS','bD','fR'],
            'D':['cD','dR','d'],
            'R':['bR','f']
        }

    def generateString(self):
        import random

        def generateFromSymbol(symbol):
            production = []
            if symbol in self.V_t:
                return symbol
            else:
                production = random.choice(self.P[symbol])
                return ''.join([generateFromSymbol(s) for s in production])
            
        return generateFromSymbol(self.S)
    
    def generate5Words( self):
        for _ in range(5):
            w = grammar.generateString()
            print("Generated string:", w)

    def toFiniteAutomaton(self):
        return FiniteAutomaton()

    def transform_grammar(self):
        productions = []

        for non_terminal, production_list in self.P.items():
            for production in production_list:
                productions.append(f"{non_terminal} -> {production}")
        return productions
    
    def classify_grammar(self, terminals, non_terminals):
        # Check if the grammar is regular
        productions = self.transform_grammar()
        is_regular = True
        for production in productions:
            left, right = production.split("->")
            left = left.strip()
            right = right.strip()
            if len(right) > 2:
                is_regular = False
                break
            if len(right) == 2 and right[0] not in non_terminals:
                is_regular = False
                break

        # Check if the grammar is context-free
        is_context_free = True
        for production in productions:
            left, right = production.split("->")
            left = left.strip()
            right = right.strip()
            if len(left) != 1:
                is_context_free = False
                break

        # Check if the grammar is context-sensitive
        is_context_sensitive = True
        for production in productions:
            left, right = production.split("->")
            left = left.strip()
            right = right.strip()
            if len(left) > len(right):
                is_context_sensitive = False
                break

        # Check if the grammar is unrestricted
        is_unrestricted = True

        # Determine the type of grammar
        if is_regular:
            return "Regular Grammar"
        elif is_context_free:
            return "Context-Free Grammar"
        elif is_context_sensitive:
            return "Context-Sensitive Grammar"
        else:
            return "Unrestricted Grammar"

class FiniteAutomaton :
    def __init__(self):
        self.Q = ['S','D','R','X']
        self.Sigma = ['a','b','c','d','f']
        self.Delta = {
            ('S', 'a'): 'S',
            ('S', 'b'): 'D',
            ('S', 'f'): 'R',
            ('D', 'c'): 'D',
            ('D', 'd'): 'R',
            ('R', 'b'): 'R',
            ('D', 'd'): 'X',
            ('R', 'f'): 'X',

        }
        self.q0 = 'S'
        self.F = {'X'}
    def stringBelongToLanguage(self,w):
        currentState = self.q0
        leng=0
        for letter in w:
            if (currentState, letter) in self.Delta:
                if (currentState, letter)==('D', 'd') and leng==len(w)-1:
                    currentState = 'X'
                    return currentState in self.F
                elif (currentState, letter)==('D', 'd'):
                    currentState = 'R'
                else:
                    currentState = self.Delta[(currentState, letter)]
            else:
                return False
            leng+=1
        return currentState in self.F

#Test Grammar functionality
grammar = Grammar()
grammar.generate5Words()

finiteAutomatom = grammar.toFiniteAutomaton()
testString1 = 'aaabd'
testString2 = 'afbbbf'
testString3 = 'afbccbbf'
print(f"\nString '{testString1}': \n Validation: {finiteAutomatom.stringBelongToLanguage(testString1)}\n")
print(f"String '{testString2}': \n Validation: {finiteAutomatom.stringBelongToLanguage(testString2)}\n")
print(f"String '{testString3}': \n Validation: {finiteAutomatom.stringBelongToLanguage(testString3)}")

gram = grammar.classify_grammar(grammar.V_t, grammar.V_n)
print(gram)