import random


RULES = 'What is the result of the expression?'


opper = ('+', '-', '*')
opperator = random.choice(opper)


def calc_question(num1, num2):

    if opperator == '+':
        correct_answer = num1 + num2

    elif opperator == '-':
        correct_answer = num1 - num2

    elif opperator == '*':
        correct_answer = num1 * num2

    return correct_answer


def get_quest_correct_answer():

    num1 = random.randint(0, 25)
    num2 = random.randint(10, 15)

    question = f'{num1} {opperator} {num2}'
    correct_answer = str(calc_question(num1, num2))

    return question, correct_answer
