def main(decimal_string):
    num = int(decimal_string)

    V1 = (num >> 0) & 0x3F
    V3 = (num >> 12) & 0xFF
    V4 = (num >> 20) & 0xF

    result = [
        ('V1', str(V1)),
        ('V3', str(V3)),
        ('V4', str(V4)),
    ]

    return result


print(main('7142254'))  # [('V1', '46'), ('V3', '207'), ('V4', '6')]
print(main('11398097'))  # [('V1', '17'), ('V3', '222'), ('V4', '10')]
print(main('14473554'))  # [('V1', '18'), ('V3', '205'), ('V4', '13')]
print(main('16283683'))  # [('V1', '35'), ('V3', '135'), ('V4', '15')]
