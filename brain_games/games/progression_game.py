from random import randint

RULES = 'What number is missing in the progression?'

START_PROG = 0
END_PROG = 100
START_STEP = 2
END_STEP = 9
START_LENGHT = 5
END_LENGHT = 10


def progress_game(step_p, lenght_p):
    result = []
    n = randint(START_PROG, END_PROG)
    for i in range(n, n + (step_p * lenght_p), step_p):
        result.append(str(i))
    return result


def get_quest_correct_answer():
    progression = progress_game(
        randint(START_STEP, END_STEP), randint(START_LENGHT, END_LENGHT)
    )

    replace = randint(START_PROG, len(progression) - 1)
    correct_answer = progression[replace]
    progression[replace] = '..'
    question = ' '.join(progression)

    return question, correct_answer
