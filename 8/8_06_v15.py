def main(decimal_str):
    decimal_num = int(decimal_str)
    F1 = (decimal_num >> 0) & 0b1
    F2 = (decimal_num >> 10) & 0b1111
    F3 = (decimal_num >> 14) & 0b1
    F4 = (decimal_num >> 15) & 0b1111
    F5 = (decimal_num >> 19) & 0b1111111111
    return F1, F2, F3, F4, F5


print(main('200125074'))  # (0, 10, 0, 11, 381)
print(main('205073673'))  # (1, 11, 0, 2, 391)
print(main('520293404'))  # (0, 3, 0, 6, 992)
print(main('3675376'))  # (0, 5, 0, 0, 7)
