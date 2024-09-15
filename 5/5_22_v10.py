import math as m


def main(arr):
    result = 0
    n = len(arr)
    for i in range(1, n + 1):
        a = 62 * arr[(n + 1 - m.ceil(i / 2)) - 1] ** 3
        b = arr[(n + 1 - i) - 1]
        result += (a - b) ** 5
    return result
