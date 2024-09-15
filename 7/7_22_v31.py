def main(x):
    x31 = {'XS': 0, 'NCL': 1}
    x01 = {'TEX': 3, 'QML': 4}
    x32 = {'XS': 2, 'NCL': x01[x[0]]}
    x33 = {'XS': 9, 'NCL': 10}
    x21 = {'GRACE': 7, 'JSON': 8, 'MUF': x33[x[3]]}
    x11 = {'NINJA': x31[x[3]], 'MTML': x32[x[3]]}
    x12 = {'NINJA': 6, 'MTML': x21[x[2]]}
    init = {'XTEND': x11[x[1]], 'x10': 5, 'SASS': x12[x[1]]}
    return init[x[4]]


print(main(['TEX', 'MTML', 'MUF', 'NCL', 'SASS']))
