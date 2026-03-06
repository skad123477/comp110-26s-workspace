"""Utility functions for working with lists."""

__author__ = "730868127"

def all(input: list[int], value: int) -> bool:
    """Return True if all elements in input equal value.
    Return False if any element does not match or if list is empty.
    """
    if len(input) == 0:
        return False

    for item in input:
        if item != value:
            return False

    return True


def max(input: list[int]) -> int:
    """Return the largest integer in input.
    Raise ValueError if input is empty.
    """
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest = input[0]

    for item in input:
        if item > largest:
            largest = item

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if list1 and list2 are deeply equal."""
    if len(list1) != len(list2):
        return False

    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True

def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending elements of list2 to it."""
    for item in list2:
        list1.append(item)

