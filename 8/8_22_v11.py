def main(x):
    f1 = x & 0b1111111111
    f2 = (x >> 10) & 0b111
    f3 = (x >> 13) & 0b111
    f4 = (x >> 16) & 0b1111111111
    return hex((f2 << 23) + (f3 << 20) + (f4 << 10) + (f1))


print(main(54560664))  # 0xcd0398
print(main(50967293))  # 0x25c26fd
print(main(49244206))  # 0x13bbc2e
print(main(60408818))  # 0x6e67f2
