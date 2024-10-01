"""Practice with coordinates"""

__author__ = "730542751"


def get_coords(xs: str, ys: str) -> None:
    countx: int = 0
    while countx < len(xs):
        county: int = 0
        while county < len(ys):
            print(xs[countx], ys[county])
            county += 1
        countx += 1
