"""Plan for a tea party by calculating quantity of tea bags, treats,  and overall cost"""

__author__: str = "730868127"


def main_planner(guests: int) -> None:
    """entrypoint of tea party program"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:$",
        cost(
            tea_count=tea_bags(people=guests),
            treat_count=treats(people=guests),
        ),
    )


def tea_bags(people: int) -> int:
    """calculates the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """calculates the number of treats needed"""
    tea_count: int = tea_bags(people=people)
    return int(tea_count * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
