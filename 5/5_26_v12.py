def main(y, x, z):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        a1 = (z[n + 1 - i-1])**2
        a2 = (x[n + 1 - i-1])**3
        res += 78 * (93 * y[i-1] + a1 + a2)**3
    return res
