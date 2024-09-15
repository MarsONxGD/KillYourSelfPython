def main(x):
    dict_x0_up = {1984: 1, 1972: 2}
    dict_x4_up = {"FLUX": 3, "SAS": 4}
    dict_x4_mid = {"FLUX": 5, "SAS": 6}
    dict_x4_down = {"FLUX": 7, "SAS": 8}
    dict_x1_up = {"TCL": 0, "SAGE": dict_x0_up[x[0]], "CLEAN": dict_x4_up[x[4]]}
    dict_x1_down = {"TCL": dict_x4_mid[x[4]], "SAGE": dict_x4_down[x[4]], "CLEAN": 9}
    dict_x3 = {1970: dict_x1_up[x[1]], 1964: dict_x1_down[x[1]]}
    dict_init = {"AGDA": 11, "GOLO": 10, "VHDL": dict_x3[x[3]]}
    return dict_init[x[2]]
