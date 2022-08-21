import prompt
import random
from brain_games.scripts.logic import random_num


print('Welcome to the Brain Games!')
name = prompt.string('May i have your name?: ')
print(f'Hello, {name}!')
print('Find the greatest common divisor of given numbers.')

def main():
    pass

def gcd(c):

    (a, b) = c

    while a != b:

        if a > b:
            a -= b
        else:
            b -= a
    return a




def brain_gcd():

    i = 0
    winstrike = 3

    while i < winstrike:

        i += 1

        num1 = random_num(20, 100)
        num2 = random_num(20, 100)

        correct_answer = gcd((num1, num2))

        try:
            print(f'Question: {num1} {num2}')
            usr_answer = prompt.string('Your answer: ')


            if int(usr_answer) == gcd((num1, num2)):
                print('Correct!')
            else:
                return print(f"'{usr_answer}'is wrong answer ;(. Correct answer was '{correct_answer}'.\nLets try again")

        except ValueError:
            return print(f"'{usr_answer}' is wrong answer ;(, {name}!")

    return 'Congratulations'


brain_gcd()
