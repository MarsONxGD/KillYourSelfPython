def main(arr):
    result = 0
    for n in arr:
        result += (22 * n**3 - 94 * n**2) ** 5
    return result
