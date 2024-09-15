def main(x):
    dict_x4_up = {"INI": 1, "XS": 2}
    dict_x4_down = {"INI": 6, "XS": 7}
    dict_x2_up = {2013: 0, 1995: dict_x4_up[x[4]], 1975: 3}
    dict_x2_down = {2013: 5, 1995: dict_x4_down[x[4]], 1975: 8}
    dict_x3 = {1992: dict_x2_up[x[2]], 2019: 4, 1959: dict_x2_down[x[2]]}
    dict_init = {"OOC": dict_x3[x[3]], "MTML": 9, "BOO": 10}
    return dict_init[x[1]]
