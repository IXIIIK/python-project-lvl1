import random
import prompt


def main():
    pass


correct_answer = ('yes', 'no')


print('Welcome to the Brain Games!')
name = prompt.string('May i have your name?: ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_game():

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
            return print(f"'yes' is wrong answer ;(.\
Correct answer was {correct_answer[1]}.\nLet's try again, {name}")
        elif usr_answer.lower() == 'no' and random_int % 2 == 0:
            return print(f"'no' is wrong answer ;(.\
Correct answer was {correct_answer[0]}.\nLet's try again, {name}")
        else:
            return print(f"{usr_answer} is wrong answer")

    if i == 3:
        print(f'Congratulations, {name}')


def main():
    even_game()


if __name__ == '__main__':
    main()
