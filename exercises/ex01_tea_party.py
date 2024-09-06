"""Plan a cozy tea party!"""

__author__: str = "730542751"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # had to remember to turn guests into str for correct output
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # looked back at Practice Memory Diagram to figure out how to call cost. Must have an argument for every parameter.


def tea_bags(people: int) -> int:
    """Determine number of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """Determine number of treats needed for the party based on number of teas"""
    return int(
        tea_bags(people=people) * 1.5
    )  # people=people because we had to call back to tea_bags and the parameter requires an aargument.


def cost(tea_count: int, treat_count: int) -> float:
    """Determine the total cost of tea bags plus treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
