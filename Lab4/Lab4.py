import random

def generateString(rule):

    string=""
    i = 0
    while i < len(rule):

        #cover case when 1 or more occurrences from options
        if rule[i] == "(" and rule[i + 1] == "+":

            for _ in range(random.randint(1, 5)):
                string += choice(options(rule[i+1:rule.index(")", i)])) 
            i = rule.index(")", i) + 1

        #cover case when 0 or more occurrences from options
        elif rule[i] == "(" and rule[i + 1] == "*":

            for _ in range(random.randint(0, 5)):
                string += choice(options(rule[i+1:rule.index(")", i)])) 
            i = rule.index(")", i) + 1
        
        #cover case when fixed occurrences from options
        elif rule[i] == "(" and rule.index(")", i) + 1 == "{":
            for i in range(int(rule.index("}", i)) - 1):
                string += choice(options(rule[i+1:rule.index(")", i)]))
            i = rule.index("}", i) + 1  
        
        #cover case when 0 or 1 occurrence from options
        elif rule[i] == "(" and rule.index(")", i) + 1 == "?" :
            if random.randint(0, 1):
                string += choice(options(rule[i+1:rule.index(")", i)])) 
            i = rule.index(")", i) + 1

        elif  i < len(rule) - 2 and rule[i + 1] == "?":
            if random.randint(0, 1):
                string += rule[i]
            i += 2

        #cover case when 1 occurrence from options
        elif rule[i] == "(":
            string += choice(options(rule[i+1:rule.index(")", i)])) 
            i = rule.index(")", i) + 1 
            

        elif rule[i] in ["|", "(", ")", "+", "*", "?", "{", "}"]:
            i += 1
            pass

        else:
            string += rule[i]
            i += 1
        
        print(i,'    ', string)
    return string

def choice(options):
    return random.choice(options)

def options(sequence):
    return sequence.split("|")

rule1 = "O(P|Q|R)+2?(3|4){" + "2}"
print(rule1)
print(generateString(rule1))