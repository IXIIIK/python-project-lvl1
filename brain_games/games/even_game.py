import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(value):
    return 'yes' if value % 2 == 0 else 'no'


def get_quest_correct_answer():
    question = random.randint(0, 100)
    correct_answer = even(question)

    return question, correct_answer
