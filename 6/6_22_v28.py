def main(O):
    D = {o ** 3 for o in O}
    X = {abs(o) for o in O if o < -97 or o >= 69}
    W = {2 * d + d % 2 for d in D if d > 56}
    s1 = sum(7 * x for x in X)
    s2 = sum(x ** 3 - w for x in X for w in W)
    return s1 + s2


print(main({1, 33, -91, -26, -87, 74, 52, 21, -68, -1}))  # 439352
print(main({-96, 68, -23, 75, 14, -14, -7, 60}))  # -222078
