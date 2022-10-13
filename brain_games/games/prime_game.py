import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
BEGIN_RANGE = 0
END_RANGE = 100


def prime(number):

    for i in range(2, number // 2):
        if number % i == 0:
            return False
            break
    else:
        return True


def get_quest_correct_answer():

    question = random.randint(BEGIN_RANGE, END_RANGE)
    if prime(question) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
