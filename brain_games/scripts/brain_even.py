import random
import prompt

def main():
    pass

print('Welcome to the Brain Games!')
name = prompt.string('May i have your name?: ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_game():

    winstrike = 3
    i = 0

    while i < winstrike:
        random_int = random.randint(0, 100)
        print(f'Question: {random_int}')
        usr_answer = prompt.string('Your answer: ')

        if usr_answer == 'yes' and random_int % 2 == 0 or (
                usr_answer == 'no' and random_int % 2 != 0):
            print('Correct!')
            i += 1
        elif usr_answer == 'yes' and random_int % 2 != 0:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}")
        elif usr_answer == 'no' and random_int % 2 == 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}")
        else:
            return print(f"{usr_answer} is wrong answer")

        random_int = random.randint(0, 100)
    return print(f'Congratulations, {name}')

main()
even_game()
