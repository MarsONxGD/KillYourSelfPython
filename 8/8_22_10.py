def main(x):
    return x[0] + (x[1]<<9) + (x[2]<<13) + (x[3]<<16)


print(main((9,3,2,225)))
