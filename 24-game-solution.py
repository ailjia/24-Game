
# define a list of 3 simplest functions
_func = [operator.add, operator.sub, operator.mul]

# use numbers except for 1
L1 = [i for i in range(2, 10)]
L2 = [i for i in range(2, 10)]

def applyToEach(L1, L2):
    """
    get all possible values through operations between L1 and L2
    """
    all = []
    for f in _func:
        for i in L1:
           for j in L2:
             temp = [f, i, j, f(i, j)]
             all.append(temp)
    return all

L3 = applyToEach(L1, L2) 

def applyMore(L3, L1):
    """
    get all possible values through operations between L3 and L1
    """
    all = []
    for f in _func:
        for i in L3:
           for j in L1:
             temp = [i[1], i[0], i[2], i[3], f, j, f(i[3], j)]
             all.append(temp)
    return all

L4 = applyMore(L3, L1) # call the function for the seocnd time between new list L3 and original list L1


def applyMoreMore(L4, L1):
     """
    get all possible values through operations between L4 and L1
    """
    all = []
    for f in _func:
        for i in L4:
           for j in L1:
             temp = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], f, j, f(i[6], j)]
             all.append(temp)
    return all

L5 = applyMoreMore(L4, L1) # call the function for the final time

# find out where the results == 24
possible_combinations = [i for i in L5 if i[9] == 24]

print(len(possible_combinations)) # chech how many possible 24-cards are there


## now the game starts

import random

choice = random.choice(possible_combinations)
number1, number2, number3, number4 = choice[0], choice[2], choice[5], choice[8]

def transform_answer(choice):
    for i in range(len(choice)):
        if str(choice[i]) == '<built-in function sub>':
            choice[i] = '-'
        if str(choice[i]) == '<built-in function add>':
            choice[i] = '+'
        if str(choice[i]) == '<built-in function mul>':
            choice[i] = '*'
    return str(choice[0:9]) + '= 24'

correct_answer = transform_answer(choice)

unshuffled_list = [number1, number2, number3, number4]
random.shuffle(unshuffled_list)

answer = input("can you make 24 out of " + str(unshuffled_list) + "? Type 'N' to show answer")

if answer == 'N':
    print correct_answer
