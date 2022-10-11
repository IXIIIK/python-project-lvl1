import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):

    for i in range(2, number // 2):
        if number % i == 0:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'

    return correct_answer


def get_quest_correct_answer():

    question = random.randint(0, 100)
    correct_answer = prime(question)

    return question, correct_answer
