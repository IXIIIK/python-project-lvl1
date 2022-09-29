import random
import prompt
from brain_games.logic.games_logic import welcome_massege


def even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def even_game():

    name = welcome_massege()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    winstrike = 3
    i = 0

    while i < winstrike:

        number = random.randint(0, 100)
        print(f'Question: {number}')
        usr_answer = prompt.string('Your answer: ')
        correct_answer = even(number)

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
