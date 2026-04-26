"""Simulate a river over time."""

__author__ = "730868127"

from river import River

if __name__ == "__main__":
    my_river = River(10, 2)
    print(my_river)
    my_river.one_river_week()
    print(my_river)
