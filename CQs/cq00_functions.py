"""Challenge Question 1"""

__author__ = "730542751"


def mimic(message: str) -> str:
    """Mimic a message back to you"""
    return message


def main() -> None:
    """Print result of calling mimic"""
    return print(mimic(message=input("""What is your message?""")))


if __name__ == "__main__":
    main()
