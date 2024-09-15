import math

def main(M):
    H = {math.ceil(u/4) + 3*u for u in M if u<=8 and u > -66}
    psi = {u**2 + u%3 for u in M if (u <= 90) != (u >= 4)}
    OMEGA = {f * h for f in psi for h in H if f >= h}
    a = len(H)
    b = sum(q for q in OMEGA)
    return a-b
