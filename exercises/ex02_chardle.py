"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730542751"


def input_word() -> str:
    """Checks if a given word has 5 characters"""
    chosen_word: str = input("Enter a 5-character word: ")
    if len(chosen_word) == 5:
        print()  # initially printed chosen_word, but removed for organization
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return chosen_word


def input_letter() -> str:
    """Checks if a given word has 1 character."""
    chosen_letter: str = input("Enter a single character: ")
    if len(chosen_letter) == 1:
        print()
    else:
        print("Error: Character must be a single character.")
        exit()
    return chosen_letter


def contains_char(word: str, letter: str) -> str:
    """Crosscheck input characters and letters"""
    matches: int = 0
    print(
        "Searching for " + letter + " in " + word
    )  # can't use previous local variables here
    if (
        word[0] == letter
    ):  # keep getting an error about subscription for return type none. fixed in lines 14 and 25
        print(letter + " found at index 0")
        matches = matches + 1
    else:
        print()
    if word[1] == letter:
        print(letter + " found at index 1")
        matches = matches + 1
    else:
        print()
    if word[2] == letter:
        print(letter + " found at index 2")
        matches = matches + 1
    else:
        print()
    if word[3] == letter:
        print(letter + " found at index 3")
        matches = matches + 1
    else:
        print()
    if word[4] == letter:
        print(letter + " found at index 4")
        matches = matches + 1
    else:
        print()
    if matches == 0:
        print("No instances of " + letter + " found in " + word)
    elif matches == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # forgot elif initially, needed instance to be singular
    else:
        print(str(matches) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
