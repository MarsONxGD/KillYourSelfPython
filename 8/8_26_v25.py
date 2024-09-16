def main(hex_str):
    int_value = int(hex_str, 16)

    A1 = (int_value >> 0) & 0b111111111
    A2 = (int_value >> 9) & 0b1111
    A3 = (int_value >> 13) & 0b1111111
    A4 = (int_value >> 20) & 0b111111111

    result = {"A1": A1, "A2": A2, "A3": A3, "A4": A4}

    return result


print(main("0x115c4d7a"))  # {'A1': 378, 'A2': 6, 'A3': 98, 'A4': 277}
print(main("0xa1bafad"))  # {'A1': 429, 'A2': 7, 'A3': 93, 'A4': 161}
print(main("0x18d34475"))  # {'A1': 117, 'A2': 2, 'A3': 26, 'A4': 397}
print(main("0x1a577b66"))  # {'A1': 358, 'A2': 13, 'A3': 59, 'A4': 421}
