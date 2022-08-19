import prompt
import random
from brain_games.scripts.logic import random_num

def main():
    pass

def brain_gcd():

    num1 = random_num(20, 100)
    num2 = random_num(20, 100)

    print(f'Question: {num1} {num2}')


    while num1 != num2:

        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
        print(num2)

brain_gcd()
