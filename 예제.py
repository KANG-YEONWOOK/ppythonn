a = ("홍길동", "고길동", "김길동", "이길동")
b = [[1,2,3,0,1],[2,3,4,0,1],[1,2,4,0,1],[3,3,4,0,1]]

for i in range(0, len(a)) :
    for j in range(0, len(b)-1) :
        b[i][3] = b[i][3] + b[i][j]

for i in range(0, len(b)) :
    for j in range(i+1, len(b)):
        if b[i][3] < b[j][3] :
            b[i][4] += 1
        elif b[i][3] > b[j][3] :
            b[j][4] += 1
        else :
            b[i][4] += 1
            b[j][4] += 1

print(b)
