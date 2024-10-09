"""Ex04- Practice with Reverse Engineering"""

__author__ = "730542751"


def all(given_list: list[int], num_given: int) -> bool:
    """Determine whether all values in the list match the given number"""
    index: int = 0
    if given_list == []:
        return False
    while index < len(given_list):
        if given_list[index] == num_given:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Find max value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    current_max: int = input[index]
    while index < len(input):
        if input[index] > current_max:
            current_max = input[index]
        index += 1
    return current_max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Determine if two lists are identical"""
    if not (len(list_1) == len(list_2)):
        return False
    else:
        index: int = 0
        while index < len(list_1):
            if list_1[index] == list_2[index]:
                index += 1
            else:
                return False
        return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Add one list to the end of another"""
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
c: list[int] = [7, 8]
