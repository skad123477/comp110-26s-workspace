"""File to define Fish class."""

__author__ = "730868127"


class Fish:
    """A Fish in the river."""

    def __init__(self) -> None:
        """Initialize a Fish with age 0."""
        self.age: int = 0

    def one_day(self) -> None:
        """Simulate one day: increase age by 1."""
        self.age += 1
