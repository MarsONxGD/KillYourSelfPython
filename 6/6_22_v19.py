import math as m


def main(B):
    E = {b % 2-3*b for b in B if b <= 17}
    P = {m.floor(b/2) for b in B if -56 < b < 49}
    F = {p % 3+m.floor(p/2) for p in P}
    return len(E.union(F))-sum(e*f for e in E for f in F)


print(main({58, 37, -92, -53, 78, -81, 81, 55, 26, 93}))  # -1354
print(main({42, -85, -51, -50, 47, 21, -1, 26, -66, -33}))  # -5158
