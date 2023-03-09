matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
M_l = []
S_l = []
row = len(matrix)
col = len(matrix[0])
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            print(i,j)
            S_l=[]
            S_l.append(i)
            S_l.append(j)
            M_l.append(S_l)

for r_c in M_l:
    for c in range(col):
        matrix[r_c[0]][c] = 0
    for r in range(row):
        matrix[r][r_c[1]] = 0
print(matrix,M_l)

"""
        row = set()
        column = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)          
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in column:
            for j in range(len(matrix)):
                matrix[j][i] = 0 """
