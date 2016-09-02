#!/usr/bin/env python3
"""The main game runner for all_things_new."""

from utils import game

def main():
    """To be run at the execution of play.py."""
    current_game = game.Game()
    while True:
        current_game.game_loop()

if __name__ == "__main__":
    main()
