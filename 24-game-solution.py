import operator

# define a list of 3 simplest functions
_func = [operator.add, operator.sub, operator.mul]

# use numbers except for 1
L = [i for i in range(2, 10)]

# can you store the result as a dictionary?? instead of a list?
## then you could retrieve the functions easier

def applyToEach(L):
    L_temp = []
    all = []
    for f in range(len(_func)):
        for i in L:
           for j in L:
             total = _func[f](i,j)
             temp = [_func[f], i, j, total]
             L_temp.append(total)  # what is the difference if the indent is reduced by 1??
             all.append(temp)
    return L_temp, all

L2, all = applyToEach(L) # can retrieve L2 by applyToEach(L)[0]

L3, all2 = applyToEach(L2) # call the function for the seocnd time

# find index of those results == 24
possible_combinations = [i for i, j in enumerate(L3) if j == 24]

# find out what are the lastest operation that gave 24
for i in possible_combinations:
    print(all2[i])

print(L3.count(24)) # find out how many 24-cards are there 

