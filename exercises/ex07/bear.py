"""File to define Bear class."""

__author__ = "730868127"


class Bear:
    """A Bear in the river."""

    def __init__(self) -> None:
        """Initialize a Bear with age 0 and hunger_score 0."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """Simulate one day: increase age by 1 and decrease hunger by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
