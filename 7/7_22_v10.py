def main(x):
    x01 = {'MQL5': 0, 'COOL': 1}
    x02 = {'MQL5': 2, 'COOL': 3}
    x21 = {'SLASH': 4, 'XML': 5}
    x31 = {'ECL': 6, 'GDB': 7}
    x03 = {'MQL5': 8, 'COOL': 9}
    x22 = {'SLASH': x01[x[0]], 'XML': x02[x[0]]}
    x04 = {'MQL5': x21[x[2]], 'COOL': x31[x[3]]}
    x32 = {'ECL': x03[x[0]], 'GDB': 10}
    init = {'EQ': x22[x[2]], 'FREGE': x04[x[0]], 'MASK': x32[x[3]]}
    return init[x[1]]


print(main(['COOL', 'MASK', 'SLASH', 'ECL']))  # 9
print(main(['COOL', 'EQ', 'SLASH', 'ECL']))  # 1
print(main(['MQL5', 'EQ', 'XML', 'GDB']))  # 2
print(main(['MQL5', 'FREGE', 'XML', 'ECL']))  # 5
print(main(['MQL5', 'FREGE', 'SLASH', 'GDB']))  # 4
