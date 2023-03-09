M_l = []
S_l = []
for i in range(5):
    S_l=[]
    for j in range(i + 1):
        if j == 0 or j == i:
            S_l.append(1)
        else:
            S_l.append(M_l[-1][j-1] + M_l[-1][j])
    M_l.append(S_l)
print(M_l)