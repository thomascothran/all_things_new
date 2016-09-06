"""Objects for our rooms"""

class Key():
    """Keys open doors."""

    def inspect(self):
        return "It's a regular key"

    def take(self):
        raise NotImplementedError