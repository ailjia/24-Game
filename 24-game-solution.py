import operator


# define a list of 3 simplest functions
_func = [operator.add, operator.sub, operator.mul]

# use numbers except for 1
L = [2, 3, 4, 5, 6, 7, 8, 9]

result = []
all = []

def applyToEach(L):
    for i in range(len(L)):
        for j in range(len(L)):
            for f in range(len(_func)):
                total = _func[f](L[i],L[j])
                temp = [_func[f], L[i],L[j], total]
                result.append(total) # what is the difference if the indent is reduced by 1??
                all.append(temp)
    return result, all

L2, all = applyToEach(L)

result2 = []

all2 = []

def applyToEach(L2):
    for i in range(len(L2)):
        for j in range(len(L2)):
            for f in range(len(_func)):
                total2 = _func[f](L2[i],L2[j])
                temp = [_func[f], L2[i], L2[j], total2]
                result2.append(total2) # what is the difference if the indent is reduced by 1??
                all2.append(temp)
    return result2, all2

L3, all2 = applyToEach(L2)

""" 
getting the index of all the result where the final outcome is 24
for i, j[3] in enumerate(all2):
    if j[3] == 24:
        print(i)
        why is there a problem?
"""

possible = []
for i, j in enumerate(L3):
    if j == 24:
        possible.append(i)

# list all possible combinations
for i in possible:
    print(all2[i])

print(L3.count(24)) # 1342