def main(fields):
    result = 0

    result |= (fields[0] & 0xFF) << 0

    result |= (fields[1] & 0x1F) << 8

    result |= (fields[2] & 0x3FF) << 13

    return result


print(main((72, 2, 556)))  # 4555336
print(main((51, 5, 345)))  # 2827571
print(main((167, 27, 522)))  # 4283303
print(main((93, 1, 200)))  # 1638749
