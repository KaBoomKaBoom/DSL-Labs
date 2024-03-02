from automathon import DFA, NFA

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
        for _, value in self.Delta.items():
            if(len(value))>1:
                return False
        return True

    def NFAtoDFA(self) :
        input_symbols = self.Sigma
        initial_state = self.q0
        states = []
        final_states = []

        transitions = {}
        new_states=[]
        for key, value in self.Delta.items():
            a, b = key
            if a not in transitions.keys():
                transitions[a] = {}
            for el in input_symbols:
                if (a, el) in self.Delta.keys():
                    transitions[a].update({el : ','.join(self.Delta[(a, el)])})
                    if len(','.join(self.Delta[(a, el)])) > 2:
                        new_states.append(','.join(self.Delta[(a, el)]))
        while new_states:
            for state in new_states:
                new_states.remove(state)
                if state not in transitions.keys():
                    transitions[state] = {}
                    temp_state = state.split(',')
                    for el in input_symbols:
                        transitions[state].update({el : ''})
                        for s in temp_state:
                            if (s, el) in self.Delta.keys():
                                transitions[state][el]+=','.join(self.Delta[(s, el)]) + ','
                                if len(','.join(transitions[state][el])) > len(','.join(state)):
                                    new_states.append(transitions[state][el].rstrip(','))
                        for key, value in transitions[state].items():
                            transitions[state][key] = value.rstrip(',')

        for el in self.F:
            transitions[el] = {}

        for key, _ in transitions.items():
            states.append(key)
        
        for el in states:
            if self.F[0] in el.split(','):
                final_states.append(el)

        print(f"Q = {states}")
        print(f"Sigma = {input_symbols}")
        print(f"Delta = {transitions}")
        print(f"q0 = {initial_state}")
        print(f"F = {final_states}")


        dfa = DFA(
            states,
            input_symbols,
            transitions,
            initial_state,
            final_states
        )
        dfa.view("DFA")


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
print("1.Grammar:")
grammar.show_gramamr()

print()

if finiteAutomatom.checkDeterministic()==False:
    print('2. Non-Deterministic Finite Automatom\n')
else:
    print('2. Deterministic Finite Automatom\n')

print("3. Deterministic Finite Automatom:")
finiteAutomatom.NFAtoDFA()

#NFA to compare graphicly with DFA
NFA({'q0','q1','q2','q3','q4'}, {'a','b'}, 
    {'q0' : {'a' : {'q1'}},
     'q1' : {'b' : {'q1'}, 'a' : {'q2'}},
     'q2' : {'b' : {'q2', 'q3'}},
     'q3' : {'b' : {'q4'}, 'a' : {'q1'}}},
     'q0', {'q4'}).view("NFA")