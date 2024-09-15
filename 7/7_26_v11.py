def main(x):
    dict_x3_up = {"NIT": 0, "ANTLR": 1, "MQL4": 2}
    dict_x0_up = {"MASK": 3, "MQL4": 4}
    dict_x0_mid = {"MASK": 5, "MQL4": 6}
    dict_x2 = {2020: dict_x0_mid[x[0]], 1989: dict_x0_up[x[0]], 1957: dict_x3_up[x[3]]}
    dict_x0 = {"MASK": 8, "MQL4": 9}
    dict_init = {1984: dict_x0[x[0]], 2018: 7, 1999: dict_x2[x[2]]}
    return dict_init[x[1]]
