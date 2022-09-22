#!/usr/bin/env python3

import prompt
import random
from brain_games.logic.games_logic import welcome_massege


def gcd(c):

    (a, b) = c

    while a != b:

        if a > b:
            a -= b
        else:
            b -= a
    return a


def brain_gcd():

    name = welcome_massege()
    print('Find the greatest common divisor of given numbers.')

    i = 0
    winstrike = 3

    while i < winstrike:

        i += 1

        num1 = random.randint(20, 100)
        num2 = random.randint(20, 100)

        correct_answer = gcd((num1, num2))

        try:
            print(f'Question: {num1} {num2}')
            usr_answer = prompt.string('Your answer: ')

            if int(usr_answer) == gcd((num1, num2)):
                print('Correct!')
            else:
                print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
                break

        except ValueError:
            return print(f"'{usr_answer}' is wrong answer ;(, {name}!")

    if i == 3:
        print(f'Congratulations, {name}!')
