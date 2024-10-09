"""Summing the elements of a list using different loops"""

__author__ = "730542751"


def w_sum(vals: list[float]) -> float:
    index: float = 0
    total: float = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for idx in vals:
        total += idx
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for idx in range(0, len(vals)):
        total += idx
    return total
