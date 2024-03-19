from circle import *


def get_perimetr(*sides):  # radius or all sides of figure
    if len(sides) == 1:
        return get_circle_perimetr(*sides)
    else:
        return sum(sides)
