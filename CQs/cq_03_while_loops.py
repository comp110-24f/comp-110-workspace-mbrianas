"""Practice using while loops"""

__author__ = "730542751"


def num_instances(phrase: str, search_char: str) -> int:
    """Count occurences of a certain character in a phrase"""
    count: int = 0
    track_index: int = 0
    while track_index < len(phrase):
        if phrase[track_index] == search_char:
            count += 1  # relative reassignment operator
        else:
            count = count
        track_index += 1
    return count  # don't forget a return value
