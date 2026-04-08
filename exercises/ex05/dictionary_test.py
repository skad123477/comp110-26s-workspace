"""Unit tests for EX05 dictionary utility functions."""

__author__ = "730868127"

import pytest
from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)


# invert test
def test_invert_use_case_basic() -> None:
    """Tests that invert swaps keys and values in a standard dictionary."""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_use_case_single_pair() -> None:
    """Tests that invert correctly handles a dictionary with one key-value pair."""
    assert invert({"hello": "world"}) == {"world": "hello"}


def test_invert_edge_case_empty() -> None:
    """Tests that invert returns an empty dictionary when given an empty dictionary."""
    assert invert({}) == {}


def test_invert_edge_case_raises_key_error() -> None:
    """Tests that invert raises a KeyError when two keys share the same value."""
    with pytest.raises(KeyError):
        invert({"alyssa": "byrnes", "adam": "byrnes"})


# favorite color test
def test_favorite_color_use_case_basic() -> None:
    """Tests that favorite_color returns the color that appears most often."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "red"}) == "blue"


def test_favorite_color_use_case_one_person() -> None:
    """Tests that favorite_color works when only one person is in the dictionary."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_favorite_color_edge_case_all_different() -> None:
    """Tests that favorite_color returns the first color when all colors appear once."""
    result: str = favorite_color({"Alice": "red", "Bob": "blue", "Charlie": "green"})
    assert result == "red"


# count test
def test_count_use_case_basic() -> None:
    """Tests that count correctly tallies each unique item in a list."""
    assert count(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def test_count_use_case_all_same() -> None:
    """Tests count when every item in the list is identical."""
    assert count(["dog", "dog", "dog"]) == {"dog": 3}


def test_count_edge_case_empty_list() -> None:
    """Tests that count returns an empty dictionary when given an empty list."""
    assert count([]) == {}


# Alphabetizwr test
def test_alphabetizer_use_case_basic() -> None:
    """Tests that alphabetizer groups words correctly under their starting letter."""
    assert alphabetizer(["banana", "apple", "avocado", "blueberry"]) == {
        "b": ["banana", "blueberry"],
        "a": ["apple", "avocado"],
    }


def test_alphabetizer_use_case_single_word_per_letter() -> None:
    """Tests alphabetizer when each word starts with a different letter."""
    assert alphabetizer(["cat", "dog", "elephant"]) == {
        "c": ["cat"],
        "d": ["dog"],
        "e": ["elephant"],
    }


def test_alphabetizer_edge_case_empty_list() -> None:
    """Tests that alphabetizer returns an empty dictionary when given an empty list."""
    assert alphabetizer([]) == {}


# UPDATE ATTENDANCE TEST
def test_update_attendance_use_case_new_day() -> None:
    """Tests that update_attendance creates a new day entry with the student."""
    log: dict[str, list[str]] = {}
    update_attendance(log, "Monday", "Alice")
    assert log == {"Monday": ["Alice"]}


def test_update_attendance_use_case_add_to_existing_day() -> None:
    """Tests that update_attendance appends a new student to an existing day."""
    log: dict[str, list[str]] = {"Monday": ["Alice"]}
    update_attendance(log, "Monday", "Bob")
    assert log == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_edge_case_no_duplicate_names() -> None:
    """Tests that update_attendance does not add a student already listed that day."""
    log: dict[str, list[str]] = {"Monday": ["Alice"]}
    update_attendance(log, "Monday", "Alice")
    assert log == {"Monday": ["Alice"]}
