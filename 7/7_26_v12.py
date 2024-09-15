def main(x):
    dict_x0 = {'MAKO': 1, 'FISH': 2, 'LASSO': 3}
    dict_x3_mid = {'ASN.1': 5, 'COQ': 6}
    dict_x3_up = {'ASN.1': 0, 'COQ': dict_x0[x[0]]}
    dict_x4 = {'XML': dict_x3_mid[x[3]], 'GLYPH': 7}
    dict_x3_down = {'ASN.1': 8, 'COQ': 9}
    dict_x1_up = {'GDB': dict_x3_up[x[3]], 'M4': 4, 'LFE': dict_x4[x[4]]}
    dict_x1_down = {'GDB': dict_x3_down[x[3]], 'M4': 10, 'LFE': 11}
    dict_init = {1974: dict_x1_down[x[1]], 2009: dict_x1_up[x[1]]}
    return dict_init[x[2]]
