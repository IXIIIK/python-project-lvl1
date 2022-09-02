#!/usr/bin/env python3

import prompt
from sympy import isprime
from brain_games.logic.games_logic import random_num


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime_game():
    i = 0
    winstrike = 3

    while i < winstrike:

        number = random_num(1, 100)
        question = f"Question: {number}"

        print(question)
        correct_answer = ('yes', 'no')
        usr_answer = prompt.string('Your answer: ')

        if isprime(number) is True and usr_answer == 'yes' or (
                isprime(number) is False and usr_answer == 'no'):
            print('Correct!')
            i += 1

        elif isprime(number) is True and usr_answer == 'no':
            print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer[0]}'.\n Let's try again, {name}!")
            break
        elif isprime(number) is False and usr_answer == 'yes':
            print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer[1]}'.\n Let's try again, {name}!")
            break
        else:
            print(f'"{usr_answer}" is wrong answer./n Let\'s try again, {name}!')
            break

    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    prime_game()


if __name__ == '__main__':
    main()
