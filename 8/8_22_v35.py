def main(x):
    valve = int(x, 16)
    x1 = (valve >> 0 & 0b1111111)
    x2 = (valve >> 7 & 0b1)
    x3 = (valve >> 8 & 0b1111111)
    x4 = (valve >> 15 & 0b1111111111)
    x5 = (valve >> 25 & 0b11111)
    result = ((x1 << 0)+(x4 << 7)+(x3 << 17)+(x2 << 24)+(x5 << 25))
    return hex(result)


print(main('0x1d616b75'))  # 0x1cd76175
print(main('0x17e29cd6'))  # 0x1739e2d6
print(main('0x903469c'))  # 0x98d031c
print(main('0x341e1ec5'))  # 0x353c1e45
