"""File to define River class."""

__author__ = "730868127"

from .bear import Bear
from .fish import Fish


class River:
    """A River ecosystem with Fish and Bears."""

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """Initialize the River with a given number of fish and bears."""
        self.day: int = 0
        self.fish: list[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: list[Bear] = [Bear() for _ in range(num_bears)]

    def __str__(self) -> str:
        """Return a string summary of the current day and populations."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def one_river_day(self) -> None:
        """Simulate a single day in the river."""
        self.day += 1
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        print(self)

    def one_river_week(self) -> None:
        """Simulate seven consecutive days in the river."""
        for _ in range(7):
            self.one_river_day()

    # Part II Methods
    def check_ages(self) -> None:
        """Remove any fish thatare older than 3 days and bears older than 5 days."""
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]

    def remove_fish(self, amount: int) -> None:
        """Remove some of fish from the front of the population."""
        self.fish = self.fish[amount:] if amount <= len(self.fish) else []

    def bears_eating(self) -> None:
        """Each bear eats 3 fish if there are at least 5 fish available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self) -> None:
        """Remove any bears with a hunger_score below 0."""
        self.bears = [b for b in self.bears if b.hunger_score >= 0]

    def repopulate_fish(self) -> None:
        """Add new fish equal to 4 times half of the current fish population."""
        new_fish = (len(self.fish) // 2) * 4
        self.fish.extend(Fish() for _ in range(new_fish))

    def repopulate_bears(self) -> None:
        """Add new bears equal to half of current bear population."""
        new_bears = len(self.bears) // 2
        self.bears.extend(Bear() for _ in range(new_bears))

    # Magic methods
    def __add__(self, other_river: "River") -> "River":
        """Combine two rivers into new river with summed populations and max day."""
        new_river = River(0, 0)
        new_river = River(0, 0)
        new_river.fish = self.fish + other_river.fish
        new_river.bears = self.bears + other_river.bears
        new_river.day = max(self.day, other_river.day)
        return new_river

    def __mul__(self, factor: int) -> "River":
        """Scale the populations of fish and bears by a given factor."""
        new_river = River(0, 0)
        new_river.fish = self.fish * factor
        new_river.bears = self.bears * factor
        new_river.day = self.day
        return new_river
