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

        #1. remove epsilon productions
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
        #initialize a copy with added prod
        P1 = self.P.copy()
        #remove eps prod from copy
        for key, value in self.P.items():
            if key in nt_epsilon and len(value) < 2:
                del P1[key]
            else:
                for v in value:
                    if v == 'eps':
                        P1[key][value].remove(v)
        
        print(f"1. After removing epsilon productions:\n{P1}")

        #2. Eliminate any renaiming (unit productions)
        #new productions for next step
        P2 = P1.copy()
        for key, value in P1.items():
            #replace unit productions
            for v in value:
                if len(v) == 1 and v in self.V_N:
                    P2[key].remove(v)
                    for p in P1[v]:
                        P2[key].append(p)
        print(f"2. After removing unit productions:\n{P2}")

        #3. Eliminate inaccesible symbols
        P3 = P2.copy()
        accesible_symbols = self.V_N
        #find elements that are inaccesible
        for key, value in P2.items():
            for v in value:
                for s in v:
                    if s in accesible_symbols:
                        accesible_symbols.remove(s)
        #remove inaccesible symbols
        for el in accesible_symbols:
            del P3[el]
        print(f"3. After removing inaccesible symbols:\n{P3}")

        #4. Remove unproductive symbols
        P4 = P3.copy()
        for key,value in P3.items():
            count = 0
            #identify unproductive symbols
            for v in value:
                if len(v) == 1 and v in self.V_T:
                    count+=1
            #remove unproductive symbols
            if count==0:
                del P4[key]
                for k, v in P3.items:
                    for e in v:
                        if k == key:
                            break
                        else:
                            if key in v:
                                P4[key].remove(v)
        print(f"4. After removing unproductive symbols:\n{P4}")

g = Gramamr()
g.chomskyNormalForm()
