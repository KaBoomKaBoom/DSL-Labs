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
    
    def generateWords( self):
        for i in range(5):
            w = grammar.generateString()
            print("Generated string:", w)

    def toFiniteAutomaton(self):
        Q = ['S','D','R','f']
        Sigma = ['a','b','c','d','f']
        Delta = {
            ('S', 'a'): 'S',
            ('S', 'b'): 'D',
            ('S', 'f'): 'R',
            ('D', 'c'): 'D',
            ('D', 'd'): 'R',
            ('R', 'b'): 'R',
            ('D', 'd'): 'd',
            ('R', 'f'): 'f',

        }
        q0 = 'S'
        F = {'d','f'}
        return FiniteAutomaton(Q, Sigma, Delta, q0, F)
    
class FiniteAutomaton :
    def __init__(self ,Q, Sigma, Delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.Delta = Delta
        self.q0 = q0
        self.F = F
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

#Test Grammar functionality
grammar = Grammar()
grammar.generateWords()
print(grammar.toFiniteAutomaton())

#Test Finite Automatum functionality
finiteAutomatom = FiniteAutomaton(grammar.toFiniteAutomaton().Q, grammar.toFiniteAutomaton().Sigma, grammar.toFiniteAutomaton().Delta, grammar.toFiniteAutomaton().q0, grammar.toFiniteAutomaton().F)
print(finiteAutomatom.stringBelongToLanguage('abdf'))
