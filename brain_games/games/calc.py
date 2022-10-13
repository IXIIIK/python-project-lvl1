import random


RULES = 'What is the result of the expression?'


def calc_question(num1, num2, opperator):

    question = f'{num1} {opperator} {num2}'

    if opperator == '+':
        correct_answer = num1 + num2

    elif opperator == '-':
        correct_answer = num1 - num2

    elif opperator == '*':
        correct_answer = num1 * num2

    return correct_answer, question


def get_quest_correct_answer():

    num1 = random.randint(0, 25)
    num2 = random.randint(10, 15)
    opper = ('+', '-', '*')
    opperator = random.choice(opper)

    question = calc_question(num1, num2, opperator)[1]
    correct_answer = str(calc_question(num1, num2, opperator)[0])

    return question, correct_answer
