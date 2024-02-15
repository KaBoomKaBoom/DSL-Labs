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
        for i in range(5):
            w = grammar.generateString()
            print("Generated string:", w)

    def toFiniteAutomaton(self):

        return FiniteAutomaton()
    
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
print(f"\nString '{testString1}': \n Validation: {finiteAutomatom.stringBelongToLanguage(testString1)}\n")
print(f"String '{testString2}': \n Validation: {finiteAutomatom.stringBelongToLanguage(testString2)}")




