"""practicing conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num<10."""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("this is the end of the function")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message if alarm is going off."""
    if alarm is True:
        return "Wake up!"
    else:
        return "Go back to sleep"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if first letter is same as letter"""
    if (word[0] == letter) is True:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="j"))
