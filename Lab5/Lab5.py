class Gramamr():
    def __init__(self):
        self.P = {
            'S' : ['dB', 'A'],
            'A' : ['d', 'dS', 'aAdAB'],
            'B' : ['aC', 'aS', 'AC'],
            'C' : ['eps'],
            'E' : ['AS']
        }
        self.V_N = ['S','A','B','C','E']
        self.V_T = ['a', 'd']
    
    def chomskyNormalForm(self):

        #remove epsilon productions

        #find non-terminal symbols that derive into empty string
        nt_epsilon = []
        for key, value in self.P.items():
            s = key
            productions = value
            for p in productions:
                if p == 'eps':
                    nt_epsilon.append(s)
        print(nt_epsilon)

    


g = Gramamr()
g.chomskyNormalForm()
