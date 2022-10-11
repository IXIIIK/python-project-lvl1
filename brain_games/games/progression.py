from random import randint

RULES = 'What number is missing in the progression?'

start_prog = 0
end_prog = 100
start_step = 2
end_step = 9
start_lenght = 5
end_lenght = 10


def progress_game(step_p, lenght_p):
    result = []
    n = randint(start_prog, end_prog)
    for i in range(n, n + (step_p * lenght_p), step_p):
        result.append(str(i))
    return result


def get_quest_correct_answer():
    progression = progress_game(
        randint(start_step, end_step), randint(start_lenght, end_lenght)
    )

    replace = randint(start_prog, len(progression) - 1)
    correct_answer = progression[replace]
    progression[replace] = '..'
    question = ' '.join(progression)

    return question, correct_answer
