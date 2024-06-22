from random import randint

class Die():
    """A simple attempt to model a die."""

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        print(f"Rolling a {self.sides} sided die...")
        return randint(1, self.sides)
    
die = Die()
print(die.roll_die())

