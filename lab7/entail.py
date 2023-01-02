variable = {'p':0, 'q':1, 'r':2}
priority = {'v': 1, '^': 2, '~': 3 }

def isoperand(c):
    return c.isalpha() and c  != 'v'
def haslessEqual(c1, c2):
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False
def toPosfix(infix):
    stack = []
    posfix = ''

    for c in infix:
        if isoperand(c):
            posfix += c
        else:
            if c =='(':
                stack.append(c)
            elif c ==')':
                operator = stack.pop()

                if operator != ')':
                    posfix += operator
                    operator = stack.pop()
            else:
                while len(stack) != 0 and haslessEqual(c, stack[-1]):
                    posfix += stack.pop()
                    
                stack.append(c)
   while len(stack) != 0:
        posfix += stack.pop()

    return posfix
def eval(post, comb):
    stack = []
    for i in post:
        if isoperand(i):
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()

            if i == '^':
                stack.append(val1 and val2)
            else:
                stack.append(val1 or val2)
    return stack.pop()
def check():
    kb=(input("Enter the knowledge base: "))
    query=(input("Enter the query: "))
    combinations=[[True,True,True],
                  [True,True,False],
                  [True,False,True],
                  [True,False,False],
                  [False,True,True],
                  [False,True,False],
                  [False,False,True],
                  [False,False,False]]

    pos_kb = toPosfix(kb)
    pos_q = toPosfix(query)

    for c in combinations:
        eval_kb = eval(pos_kb, c)
        eval_q = eval(pos_q, c)

        print(c, eval_kb, eval_q)

        if eval_kb == True:
            if eval_q == False:
                print("The knowledge base does not entail query")
                return False            
    print("Entail")
        
check()

Output:
Enter the knowledge base: (~qv~pvr)^(~q^p)^q
Enter the query: r
[True, True, True] False True
[True, True, False] False False
[True, False, True] False True
[True, False, False] False False
[False, True, True] False True
[False, True, False] False False
[False, False, True] False True
[False, False, False] False False
Entail
