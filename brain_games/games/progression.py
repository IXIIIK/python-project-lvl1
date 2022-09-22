#!/usr/bin/env python3

import prompt
import random
from brain_games.logic.games_logic import welcome_massege


def progress_game():

    name = welcome_massege()
    print('What number is missing in progression?')

    i = 0
    winstrike = 3

    while i < winstrike:

        step = random.randint(4, 6)
        numbers = list(range(1, 100, step))
        lenght = random.randint(5, 10)
        numbers = numbers[:lenght]
        x = random.choice(numbers)
        index_x = numbers.index(x)

        numbers[index_x] = '..'
        numbers = ' '.join(map(str, numbers))

        print(f'Question: {numbers}')
        usr_answer = prompt.string('Your answer: ')

        if usr_answer == str(x):
            print('Correct!')
            i += 1
        else:
            print(f'"{usr_answer}" is wrong answer ;(.\
Correct answer is "{x}".\nLet\'s try again, {name}!')
            break

    if i == 3:
        print(f'Congratulations, {name}!')
