from circle import *
from rectangle import *
from triangle import *


def get_square(*sides):
    if len(sides) == 1:
        print("Circle square")
        return get_circle_square(*sides)
    elif len(sides) == 2:
        print("Rectangle square")
        return get_rectangle_square(*sides)
    elif len(sides) == 3:
        print("Triangle square")
        return get_triangle_square(*sides)

