"""Contains the room functionality."""
import random, sys

from utils import game

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

door_colors = ('brown', 'grey', 'white', 'peach')

class Door():
    """Represents doors in a room."""
    def __init__(self, locked=None, random_choice=choose_randomly):
        # Check to see if locked is specified
        if locked == None:
            self.locked = random_choice([True, False])
        else:
            self.locked = locked
        self.deadbolt = random_choice([True, False])

    def inspect(self, level=3):
        """
        This method allows the user to inspect the door, it returns a string.

        Params:
            level: revers to the level of detail to return. Users can more or less
            closely inspect objects and get more or less detailed descriptions
        """
        return_message = ''
        if self.deadbolt:
            return_message += 'The door has a deadbolt. '
        else:
            return_message += 'The door has no deadbolt. '

        if self.locked:
            return_message += 'You try the door. It is locked. '
        else:
            return_message += 'You try the door. The knob turns, and the door cracks open'

        return return_message

    def open_object(self, room):
        if self.locked:
            return 'You try the door, but it is locked; the knob won\'t turn.'
        else:
            # TO DO: fix this so it returns user input rather than printing it
            print('The door swings open. You\'re free!')
            sys.exit()

    def __str__(self):
        return "a door"


class Room():
    """This object represents a room."""
    def __init__(self):
        self.walls = Walls()
        self.doors = [Door(locked=False), Door(locked=True)]
        self.things_in_room = [Cabinet()]


    def inspect(self, level=1):
        """
        Returns a string that describes the room
        params:
          level: refers to the detail with which the object is examined.
        """
        return (
            self.walls.inspect() + ' '
            "There are {} doors.".format(len(self.doors)) + ' ' +
            'You also see a cabinet.'
        )

    def things_inside(self, level=3, show_hidden=False, flat=True):
        """
        Returns all the things in a room.

        Params:
            level: the level of conspicuousness
            show_hidden: if True, won't return things like items in locked cabinet
            flat: returns all items as a list
        """
        if flat == True:
            things_in_room = []
            things_in_room.append(self.walls)
            for door in self.doors:
                things_in_room.append(door)
            for other_things in self.things_in_room:
                things_in_room.append(other_things)
        else:
            raise NotImplementedError
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
        self.closed = True

    def inspect(self, level=2):
        """
        Allows user to inspect the Cabinet, returns a string.

        params:
            level: refers to how closely user is looking at cabinet.
        """
        return "You see a cabinet made out of {}".format(self.material)

    def open_object(self, menu):
        """
        We want the user to be able to open the cabinet and get things inside.

        Params:
            menu: the menu object
        """
        self.closed = False
        if self.things_inside():
            menu.select_item(self.things_inside)
        else:
            return "There is nothing inside the Cabinet."

    def things_inside(self):
        """
        Returns a list of the things inside the Cabinet
        """
        return []

    def __str__(self):
        return "a cabinet"

# KEY:
# ------
