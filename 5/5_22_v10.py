import math as m


def main(arr):
    result = 0
    n = len(arr)
    for i in range(1, n + 1):
        a = 62 * arr[(n + 1 - m.ceil(i / 2)) - 1] ** 3
        b = arr[(n + 1 - i) - 1]
        result += (a - b) ** 5
    return result


print(main([0.21, 0.31, 0.3, 0.79, 0.43]))  # 5.08e+07
print(main([-0.12, -0.27, -0.11, -0.26, 0.43]))  # 5.61e+03
print(main([0.78, 0.8, 0.38, 0.42, 0.4]))  # 3.38e+03
print(main([0.82, 0.53, 0.33, -0.15, -0.81]))  # -7.23e+07
print(main([0.56, 0.49, 0.2, -0.68, 0.09]))  # -6.15e+06
