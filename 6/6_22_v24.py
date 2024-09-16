def main(X):
    B = {x ** 3 for x in X if -24 < x < 68}
    W = {x % 2 + abs(x) for x in X if x <= 88}
    T = {b - b % 2 for b in B if ((b >= -71) != (b < 3))}
    O = {w + 4 * w for w in W if ((w > -17) != (w < 26))}
    s1 = sum(T)
    s2 = sum(t * o for t in T for o in O)
    return s1 - s2


print(main({3, -88, -21, 81, -71, -38, -3, 62, -65}))  # -467118588
print(main({-28, 73, 74, -84, -49, 16, 18, 83, 88, 25}))  # -44690448
