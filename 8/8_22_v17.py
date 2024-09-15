def main1(x):
    a = int(x, 16)
    k1 = (a) & 0b11111111
    k2 = (a >> 8) & 0b11111111
    k3 = (a >> 16) & 0b1
    k4 = (a >> 17) & 0b1111
    k5 = (a >> 21) & 0b111111
    return ((k4 << 23)+(k5 << 17)+(k2 << 9)+(k3 << 8)+(k1))


def main(x):
    valve = int(x, 16)
    k1 = (valve >> 0) & 0b11111111
    k2 = (valve >> 8) & 0b11111111
    k3 = (valve >> 16) & 0b1
    k4 = (valve >> 17) & 0b1111
    k5 = (valve >> 21) & 0b111111
    result = ((k1 << 0)+(k3 << 8)+(k2 << 9)+(k5 << 17)+(k4 << 23))
    return (str(result))


print(main("0x69c7d25"),main1("0x69c7d25"))  # 124320293
print(main("0x74b425d"),main1("0x74b425d"))  # 49579357
print(main("0x1d1ab5b"),main1("0x1d1ab5b"))  # 69031771
print(main("0x4498296"),main1("0x4498296"))  # 38077846
