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
    
    def toFiniteAutomaton(self,w):
        finiteAutomatom = FiniteAutomaton()
        return finiteAutomatom.stringBelongToLanguage(w)

class FiniteAutomaton :
    def __init__(self):
        self.Q = ['S','D','R','f']
        self.Sigma = ['a','b','c','d','f']
        self.Delta = {
            ('S', 'a'): 'S',
            ('S', 'b'): 'D',
            ('S', 'f'): 'R',
            ('D', 'c'): 'D',
            ('D', 'd'): 'R',
            ('R', 'b'): 'R',
            ('D', 'd'): 'd',
            ('R', 'f'): 'f',

        }
        self.q0 = 'S'
        self.F = {'d','f'}
    def stringBelongToLanguage(self,w):
        currentState = self.q0
        leng=0
        for letter in w:
            if (currentState, letter) in self.Delta:
                if (currentState, letter)==('D', 'd') and leng==len(w)-1:
                    currentState = 'd'
                    return currentState in self.F
                elif (currentState, letter)==('D', 'd'):
                    currentState = 'R'
                else:
                    currentState = self.Delta[(currentState, letter)]
            else:
                return False
            leng+=1
        return currentState in self.F

# Instantiate Grammar
grammar = Grammar()
finiteAutomatom = FiniteAutomaton()
for i in range(5):
    w = grammar.generateString()
    print("Generated string:", w)
    s = grammar.toFiniteAutomaton(w)
    print("String belongs to language:", s)
    