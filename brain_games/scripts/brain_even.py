#!/usr/bin/env python3

from brain_games.games import even_game
from brain_games.logic.games_logic import engine_game


def main():
    engine_game(even_game)


if __name__ == '__main__':
    main()
