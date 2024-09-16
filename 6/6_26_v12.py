import math


def main(M):
    H = {math.ceil(u/4) + 3*u for u in M if u <= 8 and u > -66}
    psi = {u**2 + u % 3 for u in M if (u <= 90) != (u >= 4)}
    OMEGA = {f * h for f in psi for h in H if f >= h}
    a = len(H)
    b = sum(q for q in OMEGA)
    return a-b


print(main({-96, -64, -25, -55, 14, 79, 15, -46, 52, -68}))  # 14605980
print(main({64, -95, -30, 96, -28, -89, -56, -51, 85, 63}))  # 17969584
