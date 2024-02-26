class FiniteAutomatom:
    def __init__(self):
        self.Q = ['q0','q1','q2','q3','q4']
        self.Sigma = ['a','b']
        self.Delta = {
            ('q0', 'a') : 'q1',
            ('q1', 'b') : 'q1',
            ('q1', 'a') : 'q2',
            ('q2', 'b') : 'q2',
            ('q2', 'b') : 'q3',
            ('q3', 'b') : 'q4',
            ('q3', 'a') : 'q1'
        }
        self.q0 = 'q0'
        self.F = 'q4'

    def convert_to_grammar(self):
        S = q[0]
        V_n = self.Q
        V_t = self.Sigma
        P = []
        for state in self.S:
            for symbol in self.Sigma:
                if (state, symbol) in self.Delta:
                    next_state = self.Delta[(state, symbol)]
                    P.append((state, symbol, next_state))
        for final_state in self.F:
            P.append((final_state, '', 'e'))
        return Grammar(S, V_n, V_t, P)


class Grammar:
    def __init__(self, S, V_n, V_t, P):
        self.S = S
        self.V_n = V_n
        self.V_t  = V_t
        self.P = P

    def show_gramamr():
        print("V_n = {", ', '.join(map(str, V_n)), '}' )

a= [1,2,3,4]
print("V_n = {", ', '.join(map(str, a)), '}')    
        
              