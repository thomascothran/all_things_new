"""Controls what is printed to the screen for the user to see."""

import os

def display_to_user(menu, message=None):
    """Display to user displays the available menu, and a message below it."""
    os.system('clear')
    print('='*40)
    if menu:
        for key in sorted(menu):
            print("{}. {}".format(key, menu[key]))
    if message:
        print(message)
