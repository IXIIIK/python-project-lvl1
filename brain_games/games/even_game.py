import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
BEGIN_RANGE = 0
END_RANGE = 100

def even(value):
    return 'yes' if value % 2 == 0 else 'no'


def get_quest_correct_answer():
    question = random.randint(BEGIN_RANGE, END_RANGE)
    correct_answer = even(question)

    return question, correct_answer
