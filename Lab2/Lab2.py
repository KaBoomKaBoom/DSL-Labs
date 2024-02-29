from collections import Counter

class FiniteAutomatom:
    def __init__(self):
        self.Q = ['q0','q1','q2','q3','q4']
        self.Sigma = ['a','b']
        self.Delta = {
            ('q0', 'a') : ['q1'],
            ('q1', 'b') : ['q1'],
            ('q1', 'a') : ['q2'],
            ('q2', 'b') : ['q2', 'q3'],
            ('q3', 'b') : ['q4'],
            ('q3', 'a') : ['q1']
        }
        self.q0 = 'q0'
        self.F = ['q4']

    def convert_to_grammar(self):
        S = self.Q[0]
        V_n = self.Q
        V_t = self.Sigma
        P = []
        for state in self.Q:
            for symbol in self.Sigma:
                if (state, symbol) in self.Delta:
                    if len(self.Delta[(state, symbol)]) > 1:
                        for i in range(len(self.Delta[(state, symbol)])):
                            next_state = self.Delta[(state, symbol)][i]
                            P.append((state, symbol, next_state))
                    else:
                        next_state = self.Delta[(state, symbol)][0]
                        P.append((state, symbol, next_state))
        for final_state in self.F:
            P.append((final_state, '', 'e'))
        return Grammar(S, V_n, V_t, P)

    def checkDeterministic(self):
        counter = {}
        for key, value in self.Delta.items():
            if(len(value))>1:
                return False
        return True

    def NFAtoDFA(self) :
        col =len(self.Sigma) + 1
        deltaDFA = [[0 for _ in range(col)] for _ in range(10)]
        deltaDFA[0][0] = 'delta'
        counter = 0
        for i in range(1,col):
            deltaDFA[0][i] = self.Sigma[counter]
            counter+=1
        print(deltaDFA)

class Grammar:
    def __init__(self, S, V_n, V_t, P):
        self.S = S
        self.V_n = V_n
        self.V_t  = V_t
        self.P = P

    def show_gramamr(self):
        print("VN = {", ', '.join(map(str, self.V_n)), '}' )
        print("VT = {", ', '.join(map(str, self.V_t)), '}' )
        print("P = { ")
        for el in self.P:
            a,b,c = el
            print(f"    {a} -> {b}{c}")
        print("}")


#main
finiteAutomatom = FiniteAutomatom()
grammar = finiteAutomatom.convert_to_grammar()
# grammar.show_gramamr()

# if finiteAutomatom.checkDeterministic()==False:
#     print('Non-Deterministic Finite Automatom')
# else:
#     print('Deterministic Finite Automatom')
finiteAutomatom.NFAtoDFA()