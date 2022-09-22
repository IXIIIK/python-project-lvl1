#!/usr/bin/env python3

import prompt
import random
from brain_games.logic.games_logic import welcome_massege


def prime(number):

    question = f"Question: {number}"

    for i in range(2, number // 2):
        if number % i == 0:
            correct_answer = 'no'
            break
    else:
        correct_answer = 'yes'

    return correct_answer, question


def prime_game():

    name = welcome_massege()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    winstrike = 3

    while i < winstrike:

        number = random.randrange(0, 100)

        correct_answer = prime(number)[0]
        quest = prime(number)[1]

        print(quest)
        usr_answer = prompt.string('Your answer: ')

        if correct_answer == 'yes' and usr_answer.lower() == 'yes' or (
                correct_answer == 'no' and usr_answer.lower() == 'no'):
            print('Correct!')
            i += 1
        else:
            print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break

    if i == 3:
        print(f'Congratulations, {name}!')
