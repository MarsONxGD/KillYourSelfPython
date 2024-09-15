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
      [0.14, -0.01, 0.82, 0.41, -0.77, -0.01, 0.12, -0.52]))
