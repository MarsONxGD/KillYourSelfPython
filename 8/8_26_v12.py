def main(int_str):
    int_value = int(int_str)

    F1 = (int_value >> 0) & 0b11111
    F2 = (int_value >> 5) & 0b111111
    F3 = (int_value >> 11) & 0b1111
    F5 = (int_value >> 22) & 0b111111
    F6 = (int_value >> 28) & 0b1111
    result = (F6 << 28) + (F1 << 23) + (F3 << 19) + (F5 << 6) + (F2 << 0)

    return str(result)

# Примеры тестов
print(main("472407397"))
print(main("1818193195"))
print(main(690517051))  # Проверим результат для 690517051
print(main(3330968503)) # Проверим результат для 3330968503
