import math as m


def main(X):
    V = {m.floor(x/5)+x % 3 for x in X if x <= -62 or x >= 86}
    N = {x*v for x in X for v in V if x > v}
    F = {m.ceil(v/5) for v in V if -66 <= v < -10}
    return len(N.union(F))+sum(F)


print(main({43, -19, -48, -16, 20, 86, -74, 89, 58, -7}))  # 10
print(main({96, 35, 74, 15, -81, -9, -69, -4, -3, 30}))  # 17
