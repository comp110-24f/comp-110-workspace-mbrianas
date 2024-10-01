"""Practice with lists"""

my_numbers: list[float] = []  # literal

print(my_numbers)

my_numbers.append(1.50)  # add one item to the list

print(my_numbers)

game_points: list[int] = [102, 86, 94]
print(game_points)
# Create an already populated list

print(game_points[2])

game_points[1] = 72  # Modify elements
print(game_points)


def display(input: list[int]) -> None:
    i: int = 0
    while i < len(input):
        print(input[i])
        i += 1


print(display(input=game_points))
