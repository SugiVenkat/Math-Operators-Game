#################################
# Math operator fill sum        #
#################################
import random

mistake_count = 0
chosen1_reveal1 = []


def random_math_problem():
    #    picking a random sum from text file
    with open('mathsums.txt', 'r') as f:
        file_lines = f.readlines()
        sum_i = random.randint(0, len(file_lines)-1)
        return file_lines[sum_i][:-1]


def when_wrong(from_pt):
    global mistake_count
    print('Wrong!!!')
    mistake_count += 1
    if mistake_count >= 2:
        print('Game Over !!')
        exit()
    else:
        if from_pt == 'first':
            first_input_check()
        elif from_pt == 'second':
            second_operator_check()


def first_input_check():
    global chosen1_reveal1
    first_operator = input('Enter the first missing operator: ')
    if first_operator == chosen1[1]:
        chosen1_reveal1 = chosen1_hidden.replace('_', first_operator, 1)
        print("That's correct, You got the first operator right", chosen1_reveal1)
        second_operator_check()
    else:
        when_wrong('first')


def second_operator_check():
    global chosen1_reveal1
    second_operator = input('Now enter the second missing operator: ')
    if second_operator == chosen1[3]:
        chosen1_reveal2 = chosen1_reveal1.replace('_', second_operator, 1)
        print("That's correct again, You won", chosen1_reveal2)
    else:
        when_wrong('second')


chosen1 = random_math_problem()
chosen1_hidden = chosen1.replace('+', '_').replace('-', '_').replace('*', '_').replace('/', '_')
print('Fill in the missing operators. You have two chances. ')
print('Your math sum today is : {}'. format(chosen1_hidden))
first_input_check()


