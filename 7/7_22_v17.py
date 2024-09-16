def main(x):
    x11 = {"GOSU": 1, "LOGOS": 2}
    x12 = {"GOSU": 5, "LOGOS": 6}
    x21 = {"SAGE": 7, "KICAD": 8}
    x13 = {"GOSU": 9, "LOGOS": 10}
    x01 = {1993: 0, 1992: x11[x[1]], 2014: 3}
    x02 = {1993: x12[x[1]], 1992: x21[x[2]], 2014: x13[x[1]]}
    x22 = {"SAGE": x01[x[0]], "KICAD": 4}
    x41 = {2020: x02[x[0]], 1961: 11}
    init = {"STAN": x22[x[2]], "PONY": x41[x[4]]}
    return init[x[3]]


print(main([1993, "GOSU", "SAGE", "STAN", 1961]))  # 0
print(main([1993, 'LOGOS', 'KICAD', 'STAN', 1961]))  # 4
print(main([2014, 'LOGOS', 'KICAD', 'PONY', 2020]))  # 10
print(main([1993, 'LOGOS', 'KICAD', 'PONY', 2020]))  # 6
print(main([2014, 'GOSU', 'KICAD', 'PONY', 1961]))  # 11
