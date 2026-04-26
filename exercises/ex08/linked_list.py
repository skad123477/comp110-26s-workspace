"""Creating a singly linked-list data structure."""

__author__ = "730868127"


class Node:
    """A node in singly-linked list."""

    value: int
    next: "Node | None"

    def __init__(self, value: int, next: "Node | None") -> None:
        """Initializing."""
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        """Representation built-in."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value

    max_rest = max(head.next)
    if head.value > max_rest:
        return head.value
    else:
        return max_rest


def linkify(items: list[int]) -> Node | None:
    """Linked list of values with the same values and order as items."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where original list multiplied by factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
