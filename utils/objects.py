"""Objects for our rooms"""

class Key():
    """Keys open doors."""

    def inspect(self):
        return "It's a regular key"

    def take(self, player):
        """Take adds the item to the player's inventory"""
        player.inventory.append(self)
        return "You pick up the key."

    def __str__(self):
        return "a key"
