import prompt
import random
from brain_games.scripts.logic import random_num

opper = ('+', '-', '*')

print('Welcome to the Brain Games!')
name = prompt.string('May i have your name?: ')
print(f'Hello, {name}!')
print('What is the result of the expression?')


def main():
    pass


def calc_game():

    i = 0
    winstrike = 3

    while i < winstrike:
        i += 1

        num1 = random_num(0, 25)
        num2 = random_num(0, 10)
        correct_answer = (num1 + num2, num1 - num2, num1 * num2)
        opperator = random.choice(opper)

        try:
            calc = f'{num1} {opperator} {num2}'
            print(f'Question: {calc}')
            usr_answer = prompt.string('Your answer: ')
            usr_answer = int(usr_answer)

            if num1 + num2 == usr_answer or (
                    num1 - num2 == usr_answer) or (
                        num1 * num2 == usr_answer):
                print('Correct!')

            elif usr_answer != num1 + num2 and opperator == "+":
                print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer[0]}'.\nLet's try again, {name}!")
                break

            elif usr_answer != num1 - num2 and opperator == "-":
                print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer[1]}'.\nLet's try again, {name}!")
                break

            elif usr_answer != num1 * num2 and opperator == "*":
                print(f"'{usr_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer[2]}'.\nLet's try again, {name}!")
                break

        except ValueError:
            print(f"'{usr_answer}' is wrong answer ;(, {name}!")
            break

    if i == 3:
        print(f'Congratulations, {name}')


def main():
    calc_game()


if __name__ == '__main__':
    main()
