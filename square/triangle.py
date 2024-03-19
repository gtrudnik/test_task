def get_triangle_perimetr(a, b, c):
    return a + b + c


def get_triangle_square(a, b, c):
    p = get_triangle_perimetr(a, b, c) / 2
    return (p*(p-a)*(p-b)*(p-c)) ** 0.5


def is_rectangular(a, b, c):
    return max(a, b, c) == sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2

