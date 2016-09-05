"""The game object."""

import sys, logging

from utils.rooms import Room


# Helper functions
def get_user_input():
    """
    Get user input and returns their input. This helps with testing.
    """
    user_input = input(">> ")
    return user_input


# Classes

class Menu():
    """
    This is a generic menu option that can be used to interact
    with the game.
    """
    def __init__(self):
        self.default_prompt = {
            "l": "look around",
            "i": "inspect an object",
            "q": "quit",
        }


    def select_item(self, list_of_items, get_user_input=get_user_input):
        """
        This function takes a list of items and allows the user to select one,
        returning the item selected.

        Params:
        list_of_items is a list of items the user should be able to select.
        get_user_input specifies how to get the user's input (aids with tests)
        """
        print("Which object would you like to inspect?\nHit b to go back.")
        while True:
            for i, category in enumerate(list_of_items):
                print("{}: {}".format(i+1, str(category)))
            print("Select an item\n")
            user_input = get_user_input()
            try:
                user_input = int(user_input)
                if user_input <= len(list_of_items):
                    return list_of_items[user_input - 1]
                else:
                    print('You did not select a number corresponding to an item.')
            except TypeError:
                if user_input.lower() == 'b':
                    break

    def inspect(self, room, object=None, level=1):
        """
        This function takes an object to be inspected and prints the string.

        params:
            object: the object to be inspected
            room: the room the player is in
            level: the scrutiny the player is giving the object
        """
        if not object:
            object = self.select_item(room.things_in_room(flat=True))
        return_message = object.inspect()
        print('\n')
        print(return_message)





    def prompt_user_and_get_user_input(self, room, prompt=None):
        """
        This method takes a user's prompt, then handles the input.

            room: the room the player is in
            prompt: prompt is a dictionary with the key being the player's command
             and the value the description of what the command does.
        """
        # We need to see if any menu has been supplied
        print("="*20)
        if prompt:
            for key, value in prompt.items():
                print("{}: {}".format(key, value))
            print('='*20)
        for key, value in self.default_prompt.items():
            print ("{}: {}".format(key, value))
        print("="*20)
        user_input = input('\n>>')
        while True:
            if user_input.lower() == 'q':
                sys.exit()
            elif user_input.lower() == 'l':
                print(room.inspect())
                break
            elif user_input.lower() == 'i':
                self.inspect(room)
                break
        return True


class Game():
    """The game object keeps track of the game."""
    def __init__(self):
        self.room = Room()

    def game_loop(self):
        print(
            "\n" + "="*20 + "\n" +
            "You wake up in a room without remembering how you got " +
            "there. It is not a room you remember.\n" +
            "="*20 + "\n" +

            "Press h for a list of available commands, or q to quit."
        )
        while True:
            Menu().prompt_user_and_get_user_input(self.room)
