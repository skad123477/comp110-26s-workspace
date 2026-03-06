"""Dictionary utility functions for COMP110 EX05."""

__author__ = "730868127"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Return a new dictionary with keys and values inverted."""
    result: dict[str, str] = {}

    for key in input_dict:
        value = input_dict[key]

        if value in result:
            raise KeyError("Duplicate key found when inverting dictionary.")

        result[value] = key

    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Return the color that appears most frequently. Tie goes to first occurrence."""
    color_counts: dict[str, int] = {}
    # Count how many times each color appears

    for name in colors:
        color = colors[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_common: str = ""
    highest_count: int = 0

    for name in colors:
        color = colors[name]
        if color_counts[color] > highest_count:
            most_common = color
            highest_count = color_counts[color]

    return most_common


def count(items: list[str]) -> dict[str, int]:
    """Count how many times each item appears in the list."""
    result: dict[str, int] = {}
    # Loop through the list and update counts in the dictionary

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Return a dictionary grouping words by their first letter (lowercased)."""
    result: dict[str, list[str]] = {}

    for word in words:
        if word[0].isalpha():
            first_letter = word[0].lower()
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Add a student to the attendance list for a given day."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
