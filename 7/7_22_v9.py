def main(x):
    dict_x2 = {2003: 1, 2020: 2, 2000: 3}
    dict_x0_up = {2012: 4, 1962: 5, 2001: 6}
    dict_x4_up = {'ALLOY': 0, 'SLASH': dict_x2[x[2]], 'PAN': dict_x0_up[x[0]]}
    dict_x4_down = {'ALLOY': 9, 'SLASH': 10, 'PAN': 11}
    dict_x3 = {1973: dict_x4_up[x[4]], 1958: 7}
    dict_x0 = {2012: 8, 1962: dict_x4_down[x[4]], 2001: 12}
    dict_init = {'RUBY': dict_x3[x[3]], 'GENIE': dict_x0[x[0]], 'LATTE': 13}
    return dict_init[x[1]]


print(main([1962, 'RUBY', 2020, 1973, 'PAN']))  # 5
print(main([2001, 'LATTE', 2003, 1958, 'ALLOY']))  # 13
print(main([1962, 'GENIE', 2003, 1958, 'SLASH']))  # 10
print(main([2001, 'GENIE', 2020, 1958, 'ALLOY']))  # 12
print(main([1962, 'RUBY', 2000, 1973, 'SLASH']))  # 3
