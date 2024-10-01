"""Ex03-Wordle. Adapted from the NYT"""

__author__ = "730542751"


def input_guess(secret_word_len: int) -> str:
    """Set up proper guess length"""
    chosen_word: str = input(f"Enter a {secret_word_len} character word: ")
    while not (len(chosen_word) == secret_word_len):
        chosen_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return chosen_word


def contains_char(unknown_word: str, chosen_char: str) -> bool:
    """Determine if the unknown word contains a guessed character"""
    assert len(chosen_char) == 1
    index: int = 0
    while index < len(unknown_word):
        if unknown_word[index] == chosen_char:
            return True
        else:
            # can return true as soon as character is found,
            # regardless of other characters
            index += 1
    return False


def emojified(chosen: str, unknown: str) -> str:
    """Determines whether any characters of the user guess match the secret word"""
    assert len(chosen) == len(unknown)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""  # required for concatenation
    while index < len(unknown):
        if chosen[index] == unknown[index]:
            result += GREEN_BOX  # otherwise, end up with vertical
            index += 1
        elif not (unknown[index] == chosen[index]) and contains_char(
            unknown, chosen[index]
        ):
            result += YELLOW_BOX
            index += 1
        elif not (contains_char(unknown, chosen[index])):
            result += WHITE_BOX
            index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1
    total_tries: int = 6
    while current_turn <= total_tries:  # need to add not won yet
        print(f"=== Turn {current_turn}/{total_tries} ===")
        current_guess: str = input_guess(len(secret))
        if current_guess == secret:
            print(emojified(secret, secret))
            print(f"You won in {current_turn}/{total_tries} turns!")
            return
        else:
            print(emojified(current_guess, secret))
            current_turn += 1
    if current_turn > 6:
        print(f"X/{total_tries} - Sorry, try again tomorrow!")
        return


# Went to office hours for help, needed to add current_guess variable
# and needed it to be inside while loop

if __name__ == "__main__":
    main(secret="codes")
