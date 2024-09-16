def main(x):
    dict_x2_up = {"SWIFT": 0, "SLIM": 1, "RUST": 2}
    dict_x4_mid = {1976: 4, 1975: 5}
    dict_x2_down = {"SWIFT": 9, "SLIM": 10, "RUST": 11}
    dict_x4_up = {1976: dict_x2_up[x[2]], 1975: 3}
    dict_x1_down = {"HACK": dict_x2_down[x[2]], "DM": 12, "ORG": 13}
    dict_x1 = {"HACK": dict_x4_up[x[4]], "DM": dict_x4_mid[x[4]], "ORG": 6}
    dict_x4 = {1976: 8, 1975: dict_x1_down[x[1]]}
    dict_init = {2006: dict_x1[x[1]], 1990: 7, 1989: dict_x4[x[4]]}
    return dict_init[x[3]]


print(main([2012, 'HACK', 'RUST', 1990, 1976]))  # 7
print(main([2012, 'HACK', 'SWIFT', 1989, 1976]))  # 8
print(main([2012, 'DM', 'SWIFT', 2006, 1976]))  # 4
print(main([2012, 'ORG', 'SWIFT', 1989, 1975]))  # 13
print(main([2012, 'DM', 'SWIFT', 1989, 1975]))  # 12
