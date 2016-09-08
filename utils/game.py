"""The game object."""

import sys, logging, os, time

from utils.rooms import Room
from utils import objects
from utils import hud


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
    def __init__(self, game=None):
        """
        Initializes the menu

        params:
            game: is the current game, It is optional, because it often isn't needed
        """
        self.game = game
        self.default_prompt = {
            "l": "look around",
            "i": "inspect an object",
            "o": "open something",
            "q": "quit",
            "t": "take",
        }

    def select_item(self, list_of_items, get_user_input=get_user_input):
        """
        This function takes a list of items and allows the user to select one,
        returning the item selected.

        Params:
        list_of_items is a list of items the user should be able to select.
        get_user_input specifies how to get the user's input (aids with tests)
        """
        print("Which object would you like to select?\nHit b to go back.")
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
            except ValueError:
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
        try:
            if not object:
                object = self.select_item(room.things_inside(flat=True))
            return_message = object.inspect()
            hud.display_to_user(self.default_prompt, return_message)
        except AttributeError:
            print('Going back')

    def open_object(self, room, player, object=None):
        """
        This function allows you to open things.
        """
        try:
            if not object:
                object = self.select_item(room.things_inside(flat=True))
            return_message = object.open_object(self, player)
            print('\n')
            print(return_message)
        except AttributeError:
            print("You can't open that.")

    def take_object(self, room, player, object=None):
        """
        This function allows you to take things and add them to your inventory.
        """
        try:
            if not object:
                object = self.select_item(room.things_inside(flat=True))
            return_message = object.take(player=player)
            print(return_message)
        except AttributeError:
            print('You cannot take that.')

    def prompt_user_and_get_user_input(self, room, prompt=None, get_user_input=get_user_input, message=None):
        """
        This method takes a user's prompt, then handles the input.

            room: the room the player is in
            prompt: prompt is a dictionary with the key being the player's command
             and the value the description of what the command does.
            get_user_input is the function we use to get the user's input
        """

        # We need to add default menu if none supplied
        if not prompt:
            prompt=self.default_prompt

        hud.display_to_user(menu=prompt, message=message)
        user_input = get_user_input()

        if user_input.lower() == 'q':
            sys.exit()
        elif user_input.lower() == 'b':
            pass
        elif user_input.lower() == 'l':
            self.prompt_user_and_get_user_input(room, message=room.inspect())
        elif user_input.lower() == 'i':
            self.inspect(room)
        elif user_input.lower() == 'o':
            self.open_object(room, self.game.player)
        elif user_input.lower() == 't':
            # TO DO: Handle picking up objects
            try:
                self.take_object(room, player=self.game.player)
            except Exception as e:
                print('Error: ', e)
                sys.exit()

class Game():
    """The game object keeps track of the game."""
    def __init__(self):
        self.room = Room()
        self.player = Player()

    def game_loop(self):
        message = (
            "You wake up in a room without remembering how you got " +
            "there. It is not a room you remember.\n" +
            "Press h for a list of available commands, or q to quit. " +
            "Hit any key to start"
        )
        hud.display_to_user(menu=None, message=message)
        user_input = get_user_input()
        if user_input.lower() == 'q':
            sys.exit()
        while True:
            Menu(game=self).prompt_user_and_get_user_input(self.room)


class Player():
    """The player object"""
    def __init__(self):
        self.inventory = []
        self.health = 100

    def attack(self, opponent, attack_strength=40):
        opponent.health -= attack_strength
        # TO DO: Refactor so we're not directly using print
        if opponent.health > 0:
            print('You attack. Opponent health is {}'.format(opponent.health))
        else:
            print('You won!')


class Battle():
    """Controls battles"""
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def battle_loop(self):
        # Next tells who's up to attack
        next_attacker = self.player
        next_attacked = self.opponent

        while self.player.health > 0 and self.opponent.health > 0:
            time.sleep(1)
            next_attacker.attack(next_attacked)
            time.sleep(1)
            next_attacker, next_attacked = next_attacked, next_attacker

