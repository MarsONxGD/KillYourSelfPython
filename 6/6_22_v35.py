import math as m


def main(L):
    E = {((m.floor(l/6))-(l**3)) for l in L if ((l > (-72)) or (l <= 28))}
    O = {m.floor(l/4) for l in L if ((l > 33) and (l < 99))}
    J = {(o*e) for o in O for e in E if (o <= e)}
    a = sum((m.floor(e/6))for e in E)
    b = sum((abs(e) + m.ceil(v/9)) for e in E for v in J)
    result = a + b
    return result


print(main({-96, 64, -61, 4, -91, -17, 49, 23, 90, -69}))  # 172121597
print(main({96, 1, -62, 16, 49, -78, -76, -39, -4, -33}))  # 76968098
