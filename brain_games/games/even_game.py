#!/usr/bin/env python3

import random
import prompt
from brain_games.logic.games_logic import welcome_massege


correct_answer = ('yes', 'no')


def even_game():

    name = welcome_massege()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    winstrike = 3
    i = 0

    while i < winstrike:
        i += 1

        random_int = random.randint(0, 100)
        print(f'Question: {random_int}')
        usr_answer = prompt.string('Your answer: ')

        if usr_answer.lower() == 'yes' and random_int % 2 == 0 or (
                usr_answer.lower() == 'no' and random_int % 2 != 0):
            print('Correct!')
        elif usr_answer.lower() == 'yes' and random_int % 2 != 0:
            print(f"'yes' is wrong answer ;(.\
Correct answer was '{correct_answer[1]}'.\nLet's try again, {name}!")
            break
        elif usr_answer.lower() == 'no' and random_int % 2 == 0:
            print(f"'no' is wrong answer ;(.\
Correct answer was '{correct_answer[0]}'.\nLet's try again, {name}!")
            break
        else:
            print(f"{usr_answer} is wrong answer")
            break

    if i == 3:
        print(f'Congratulations, {name}!')
