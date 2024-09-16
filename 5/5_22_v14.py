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


print(main([0.06, -0.82, -0.09, -0.24, 0.92], [-0.13, 0.49, 0.73,
      0.41, -0.52], [0.53, 0.93, 0.89, -0.11, -0.22]))  # 5.48e+13
print(main([0.25, 0.82, -0.86, -0.41, -0.3], [-0.54, 0.37, -
      0.13, -0.97, 0.91], [0.38, -0.27, 0.51, 0.26, -0.09]))  # 1.00e+12
print(main([-0.78, 0.85, 0.38, -0.64, 0.88], [0.06, 0.64, -0.87, -
      0.81, -0.06], [-0.9, -0.62, -0.11, 0.97, -0.54]))  # 1.47e+14
print(main([0.86, 0.96, -0.54, -0.96, -0.68], [-0.15, -0.69, -0.76,
      0.23, -0.71], [-0.13, -0.2, 0.8, 0.2, -0.12]))  # 8.18e+09
print(main([-0.21, -0.73, 0.31, 0.13, 0.05], [-0.93, 0.51, -0.52,
      0.5, 0.39], [0.8, 0.86, 0.64, 0.65, 0.49]))  # 1.11e+14
