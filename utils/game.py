"""The game object."""

import sys

from utils.rooms import Room


class Menu():
    """
    This is a generic menu option that can be used to interact
    with the game.
    """
    def __init__(self):
        self.default_prompt = (
            """
            l: look around
            q: quit
            """
        )

    def prompt_user_and_get_user_input(self, room):
        print(self.default_prompt)
        user_input = input('\n')
        if user_input.lower() == 'q':
            sys.exit()
        if user_input.lower() == 'l':
            print(room.description())
        return True


class Game():
    """The game object keeps track of the game."""
    def __init__(self):
        self.room = Room()

    def game_loop(self):
        print(
            """You wake up in a room without remembering how you got
            there. It is not a room you remember.

            Press h for a list
            of available commands, or q to quit."""
        )
        while True:
            user_input = 'l'
