"""Contains the room functionality."""
import random

# TO DO: Fix global variables
wall_colors = [
    'white',
    'dark brown',
]
wall_conditions = [
    'recently painted',
    'peeling',
    'dingy'
]


class Walls():
    """A class representing the walls for room."""

    def __init__(self):
        """Init is randomly generating a wall."""
        self.color = random.choice(wall_colors)
        self.condition = random.choice(wall_conditions)

    def description(self):
        return "The walls are {} and {}.".format(
            self.color, self.condition
        )

    def __str__(self):
        return self.description()

class Door():
    """Represents doors in a room."""
    def __init__(self):
        self.locked = random.choice([True, False])
        self.deadbolt = random.choice([True, False])

    def __str__(self):
        return "a door"


class Room():
    """This object represents a room."""
    def __init__(self):
        self.walls = Walls()
        self.doors = [Door(), Door(),]




