def main(x):
    x21 = {'OPAL': 0, 'GOSU': 1}
    x11 = {2008: 2, 2001: 3}
    x12 = {2008: 6, 2001: 7}
    x22 = {'OPAL': 9, 'GOSU': 10}
    x31 = {'XSLT': x21[x[2]], 'ANTLR': x11[x[1]], 'SCAML': 4}
    x23 = {'OPAL': 5, 'GOSU': x12[x[1]]}
    x41 = {1969: x22[x[2]], 1973: 11, 1994: 12}
    x42 = {1969: x31[x[3]], 1973: x23[x[2]], 1994: 8}
    x13 = {2008: x41[x[4]], 2001: 13}
    init = {'ROUGE': x42[x[4]], 'JAVA': x13[x[1]]}
    return init[x[0]]


print(main(['ROUGE', 2008, 'GOSU', 'XSLT', 1994]))  # 8
print(main(['JAVA', 2001, 'GOSU', 'ANTLR', 1994]))  # 13
print(main(['JAVA', 2008, 'GOSU', 'ANTLR', 1969]))  # 10
print(main(['ROUGE', 2001, 'OPAL', 'SCAML', 1973]))  # 5
print(main(['JAVA', 2008, 'OPAL', 'SCAML', 1973]))  # 11
