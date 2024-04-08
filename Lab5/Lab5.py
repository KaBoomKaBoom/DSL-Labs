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
        
        for key, value in self.P.items():
            #traverse each non-terminal that has epsilon production
            for ep in nt_epsilon:
                #traverse each production 
                for v in value:
                #check non-erminal with eps prod is in current production
                    prod_copy = v
                    if ep in prod_copy:
                        for c in prod_copy:
                            #delete epsilon prod and add new prod
                            if c == ep:
                                value.append(prod_copy.replace(c, ''))
        for key, value in self.P.items():
            if key in nt_epsilon and len(value) < 2:
                del self.P[key]
            else:
                for v in value:
                    if v == 'eps':
                        value.remove(v)
        print(self.P)

    


g = Gramamr()
g.chomskyNormalForm()
