def main(int_str):
    int_value = int(int_str)

    F1 = (int_value >> 0) & 0b11111
    F2 = (int_value >> 5) & 0b111111
    F3 = (int_value >> 11) & 0b1111
    F5 = (int_value >> 22) & 0b111111
    F6 = (int_value >> 28) & 0b1111
    result = (F6 << 28) + (F1 << 23) + (F3 << 19) + (F5 << 6) + (F2 << 0)

    return str(result)


print(main("472407397"))  # 316148779
print(main("1818193195"))  # 1709706345
print(main("690517051"))  # 770705697
print(main("3330968503"))  # 3414689437
