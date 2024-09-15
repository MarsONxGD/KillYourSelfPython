def main(hex_str):
    int_value = int(hex_str, 16)

    A1 = (int_value >> 0) & 0b111111111
    A2 = (int_value >> 9) & 0b1111
    A3 = (int_value >> 13) & 0b1111111
    A4 = (int_value >> 20) & 0b111111111

    result = {"A1": A1, "A2": A2, "A3": A3, "A4": A4}

    return result

