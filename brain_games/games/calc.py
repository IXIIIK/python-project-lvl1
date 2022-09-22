#!/usr/bin/env python3

import prompt
import random
from brain_games.logic.games_logic import welcome_massege

opper = ('+', '-', '*')
opperator = random.choice(opper)


def calc_question(num1, num2):

    if opperator == '+':
        correct_answer = num1 + num2

    elif opperator == '-':
        correct_answer = num1 - num2

    elif opperator == '*':
        correct_answer = num1 * num2

    return correct_answer


def calc_game():

    name = welcome_massege()
    print('What is the result of the expression?')

    i = 0
    winstrike = 3

    while i < winstrike:

        num1 = random.randint(0, 25)
        num2 = random.randint(0, 10)
        question = f'{num1} {opperator} {num2}'
        correct_answer = calc_question(num1, num2)

        print(f'Question: {question}')
        usr_answer = prompt.string('Your answer: ')

        if int(usr_answer) == correct_answer:
            print('Correct!')
            i += 1

        elif usr_answer == str(usr_answer):
            print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break

    if i == 3:
        print(f'Congratulations, {name}!')
