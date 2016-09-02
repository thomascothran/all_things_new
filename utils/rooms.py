"""Contains the room functionality."""
import random

####################
# Helper functions#
##################

def choose_randomly(choices):
    """Set this as a separate variable to make testing easer"""
    return random.choice(choices)


# WALLS
# ----------------------
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

    def __init__(self, random_choice=choose_randomly):
        """Init is randomly generating a wall."""
        self.color = random_choice(wall_colors)
        self.condition = random_choice(wall_conditions)

    def inspect(self):
        return "The walls are {} and {}.".format(
            self.color, self.condition
        )

    def __str__(self):
        return "a wall"


# DOORS
# --------------

door_colors = ('brown', 'grey')

class Door():
    """Represents doors in a room."""
    def __init__(self, random_choice=choose_randomly):
        self.locked = random_choice([True, False])
        self.deadbolt = random_choice([True, False])


    def inspect(self, level=3):
        """
        This method allows the user to inspect the door, it returns a string description.

        Params:
            level: revers to the level of detail to return. Users can more or less
            closely inspect objects and get more or less detailed descriptions
        """

    def __str__(self):
        return "a door"


class Room():
    """This object represents a room."""
    def __init__(self):
        self.walls = Walls()
        self.doors = [Door(), Door(),]

    def inspect(self, level=1):
        """
        Returns a string that describes the room
        params:
          level: refers to the detail with which the object is examined.
        """
        return (
            self.walls.inspect() + ' '
            "There are {} doors.".format(len(self.doors))
        )

    def things_in_room(self, level=3, show_hidden=False):
        """
        Returns all the things in a room.

        Params:
            level: the level of conspicuousness
            show_hidden: if True, won't return things like items in locked cabinet
        """
        things_in_room = {
            'walls': (self.walls),
            'doors': (self.doors)
        }
        return things_in_room

# CABINETS:
# -------------

cabinet_material = ['old wood', 'maple']

class Cabinet():
    """
    This represents a cabinet class, which goes in a room.
    """
    def __init__(self, random_choice=choose_randomly):
        self.material = random_choice(cabinet_material)

    def inspect(self, level=2):
        """
        Allows user to inspect the Cabinet, returns a string.

        params:
            level: refers to how closely user is looking at cabinet.
        """
        return "a cabinet made out of {}".format(self.material)

    def __str__(self):
        return "a cabinet"

