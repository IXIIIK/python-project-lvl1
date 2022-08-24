#!/usr/bin/env python3

import prompt
import random
from brain_games.scripts.logic import random_num


def progress():

        num1 = random_num(5, 10)
        num2 = random_num(23, 40)
        step = random_num(2, 4)
        progress = ''

        for i in range(num1, num2, step):
            progress += str(i)
            progress += ' '

            progress[step] = '..'

            i += 1
        return progress



def progress_game():

    progress()


def main():
    progress_game()


if __name__ == "__main__":
    main()
