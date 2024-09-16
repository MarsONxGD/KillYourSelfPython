import math as m


def main(z, y):
    n = len(z)
    result = 0
    for i in range(1, n+1):
        a = y[(n+1-m.ceil(i/4))-1]
        b = z[m.ceil(i/3)-1]**3
        result += (72*(m.log10(a + 1 + b))**4)
    return 24*result


print(main([-0.45, -0.43, -0.49, 0.58, -0.29, -0.89, -0.02, -0.41],
      [0.14, -0.01, -0.82, 0.41, -0.77, -0.01, -0.12, -0.52]))  # 1.91e+02
print(main([0.74, 0.33, 0.61, 0.04, 0.48, 0.68, 0.52, -0.82],
      [-0.09, -0.72, -0.23, 0.94, 0.97, 0.6, -0.2, -0.15]))  # 6.32e-01
print(main([-0.38, -0.49, 0.18, 0.45, -0.36, 0.14, -0.43, 0.07],
      [-0.18, 0.19, 0.78, -0.34, -0.44, 0.05, -0.03, 0.39]))  # 1.57e+00
print(main([-0.35, -0.01, 0.64, -0.26, 0.09, 0.15, -0.75, -0.35],
      [-0.89, 0.76, -0.59, -0.36, 0.71, 0.83, -0.12, 0.59]))  # 9.60e+00
print(main([0.38, 0.08, -0.42, 0.03, -0.68, -0.83, 0.48, 0.75],
      [-0.75, -0.55, -0.17, 0.61, 0.41, 0.61, 0.22, 0.09]))  # 3.01e-01
