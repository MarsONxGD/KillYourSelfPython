def main(hex_str):
    int_value = int(hex_str, 16)

    X1 = (int_value >> 0) & 0b1111111
    X2 = (int_value >> 7) & 0b1111111111
    X3 = (int_value >> 17) & 0b11
    X4 = (int_value >> 19) & 0b11111111
    X5 = (int_value >> 27) & 0b1111111

    result = (X5 << 27) + (X3 << 25) + (X4 << 17) + (X1 << 10) + (X2 << 0)

    return result

print(main("0xc5dc46e1"))  # 3312944269
print(main("0x7b4f6696"))  # 2127715021
print(main("0x1feb07000"))  # 8483766496
print(main("0x131515e48"))  # 5105853116
