"""Mutating functions."""

__author__ = "730542751"

a: list[int] = [1, 2, 3]
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(given_list: list[int], added_number: int) -> None:
    given_list.append(added_number)


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[index] = list[index] * 2
        index += 1


double(list_2)
print(list_1)
print(list_2)
