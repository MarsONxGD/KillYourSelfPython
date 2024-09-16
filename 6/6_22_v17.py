def main(A):
    W = {a for a in A if -6 < a}
    E = {a for a in A if a <= 87}
    K = {6*e for e in E if e < 54}
    O = {w*k for w in W for k in K if w >= k}
    return sum(K)-sum(k*o for k in K for o in O)


print(main({-64, -32, 34, 4, -85, 13, -46, -77, -72, 94}))  # -617598150
print(main({-95, 67, -60, -89, -87, -20, 53, -43, -42, 21}))  # -801157404
