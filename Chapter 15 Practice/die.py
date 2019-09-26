from random import randint


class Die:
    """A class that creates a die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll_die(self):
        """Rolls the die from 1 to the number of sides the die has."""
        return randint(1, self.num_sides)
