import math as m


def main(x, z, y):
    result = 0
    n = len(x)
    for i in range(1, n + 1):
        a = 70 * y[(m.ceil(i / 4)) - 1]
        b = z[(n + 1 - i) - 1] ** 2
        c = x[(n + 1 - m.ceil(i / 3)) - 1] ** 3
        result += 9 * (a + b + c) ** 6
    return 69 * result
