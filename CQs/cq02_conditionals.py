"""Write a simple number guessing game"""

__author__: str = "730542751"


def guess_a_number() -> None:
    """Main program for guessing game"""
    secret: int = 7
    guess: int = int(input("Guess a number: "))  # convert str to int
    print("Your guess was " + str(guess))
    if secret == guess:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
