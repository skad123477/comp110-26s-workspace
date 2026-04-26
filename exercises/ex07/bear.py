"""File to define Bear class."""

__author__ = "730868127"


class Bear:
    """A bear in the river simulation."""

    def __init__(self) -> None:
        """Initialize a bear with age 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulate one day where age increases by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Simulate bear eating fish."""
        self.hunger_score += num_fish
