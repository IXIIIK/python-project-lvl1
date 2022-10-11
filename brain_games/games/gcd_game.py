import random


RULES = 'Find the greatest common divisor of given numbers.'


def gcd(c):

    (a, b) = c

    while a != b:

        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_quest_correct_answer():

    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    question = f'{num1} {num2}'
    correct_answer = str(gcd((num1, num2)))

    return question, correct_answer
