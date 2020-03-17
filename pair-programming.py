'''

24-game gives the player 4 numbers, and ask for player to use operations +, -, * on these numbers
in a way that the result equals to 24

'''
import operator
import random
import itertools

class number_set():

    def __init__(self, a, b, c, d):

        self.numbers = [a, b, c, d]

    def start_game(self):
        print('Wecome to the game. here are the {0}'.format(self.numbers))

    def user_input(self):
        ask_for_input = input("please give 3 operations (possible: add for +, sub for -, mul for *) in the order, separate by comma") # add, sub, mul

        while not(len(ask_for_input) == 13):
            ask_for_input = input("please check if the operations are correct")

        return ask_for_input

    def split(self, user_input):
        x,y,z = user_input.split(',')

        return [x.replace(' ', ''),y.replace(' ', ''),z.replace(' ', '')]

    def operators(self, operators):

        _func = {'add': operator.add,  # add
                 'sub': operator.sub,  # substract
                 'mul': operator.mul  # multiplication
                 }

        self.f1 = _func[operators[0]]
        self.f2 = _func[operators[1]]
        self.f3 = _func[operators[2]]

    def calculate(self):
        self.result1 = self.f1(self.numbers[0], self.numbers[1])
        self.result2 = self.f2(self.result1, self.numbers[2])
        self.result3 = self.f3(self.result2, self.numbers[3])
        return self.result3

    def check_answer(self, result3):
        if self.result3 == 24:
            print('Correct')

        trial = 0
        while self.result3 != 24:
            print("The current answer is {}. Enter 'T' to try again. Enter 'N' to shower answer".format(self.result3))
            choice = input()
            if choice == 'T' and trial <= 3:
                trial += 1
                user_operations = self.user_input()
                user_operations = self.split(user_operations)
                self.operators(user_operations)
                self.result3 = self.calculate()
                #print("The current answer is {}. Enter 'T' to try again. Enter 'N' to shower answer".format(self.result3))
            if choice == 'T' and trial > 3:
                print('you have reached total number of trials')
                print(answer)
            else:
                print(answer)
                break

def generate_answers():
    list_all_num = list(itertools.combinations_with_replacement(range(1, 10), 4))
    #print(len(list_all_num))

    ops = ['add', 'sub', 'mul']
    list_all_ops = list(itertools.combinations_with_replacement(ops, 3))
    #print(list_all_ops)

    possible_cases = []
    all_answers = []
    for i in list_all_num:
        test = number_set(*i)
        for j in list_all_ops:
            user_operations = j
            test.operators(user_operations)
            temp = test.calculate()
            if temp == 24:
                possible_cases.append(i)
                all_answers.append([i, j])

    return possible_cases, all_answers

if __name__ == '__main__':
    possible_cases, all_answers = generate_answers()

    choice = random.choice(possible_cases)
    answer_index = possible_cases.index(choice)
    answer = all_answers[answer_index] # save the answer

    test = number_set(*choice)
    test.start_game()

    user_operations = test.user_input()
    user_operations = test.split(user_operations)
    test.operators(user_operations)

    result = test.calculate()
    test.check_answer(result)


