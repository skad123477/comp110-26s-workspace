"""EX03 - Wordle - A model of the Wordle game."""

__author__ = "730868127"

WHITE_BOX: str = "\U00002b1c"  # this represents the white box emoji
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(
    secret_word_length: int,
) -> str:  # creates the function to prompt the user to enter the guess.
    """Prompt user to enter a guess that is the correct length and return it."""
    guess: str = input(f"Enter a {secret_word_length} character word: ")

    # this is a while loop that keeps prompting the user to enter a guess
    # until it is the correct length of characters.
    while len(guess) != secret_word_length:
        guess = input(f"That wasn't {secret_word_length} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Return True if char_guess is found anywhere in secret_word."""
    assert (
        len(char_guess) == 1
    )  # Makes sure that char_guess is just a single character.
    idx: int = 0  # idx is short for index, initializes to start at 0.

    while idx < len(
        secret_word
    ):  # this loop as long as idx is less than the length of secret_word
        if secret_word[idx] == char_guess:
            return True
        idx += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis that represent the accuracy of the guess."""
    assert len(guess) == len(secret)

    idx: int = 0
    result: str = ""

    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[idx]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX

        idx += 1
    return result


def main(secret: str) -> None:
    """This is the entrypoint and main loop of the game."""
    turns_taken: int = 0
    max_turns: int = 6
    won: bool = False

    while turns_taken < max_turns and not won:
        turns_taken += 1  # adds 1 to turns_taken each time the loop runs.
        print(f"=== Turn {turns_taken}/{max_turns} ===")
        guess: str = input_guess(len(secret))

        emoji_result: str = emojified(guess, secret)
        print(
            emoji_result
        )  # prints the string of emojis to represent the accuracy of the guess.

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turns_taken}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
