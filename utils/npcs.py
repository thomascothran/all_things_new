"""Monsters to scare us."""

import sys

class Monster():
    """This is to be used as a base class for other monsters"""
    def __init__(self):
        self.health = 100

    def attack(self, player, attack_strength=30):
        """
        In this function, the vampire attacks the player

        Params:
            attack_strength is how many health points the monster takes from the player
        """
        player.health -= attack_strength
        # TO DO: Refactor so that we're not using print directly
        if player.health > 0:
            print('The monster attacked. Player health is {}'.format(player.health))
        else:
            print('The monster killed you.')
            sys.exit()


