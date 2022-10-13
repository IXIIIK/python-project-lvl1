#!/usr/bin/env python3

import prompt

ROUND_COUNT = 3


def run_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULES)
    start = 0

    while start < ROUND_COUNT:
        question, correct_answer = game.get_quest_correct_answer()

        print(f'Question: {question}')
        usr_answer = prompt.string('Your answer: ')

        if usr_answer == correct_answer:
            print('Correct!')
            start += 1
        else:
            print(
                f"'{usr_answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}!"
            )
            break

    else:
        print(f'Congratulations, {name}!')
