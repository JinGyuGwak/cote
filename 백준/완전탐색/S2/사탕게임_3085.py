n = int(input())

a = []
for _ in range(n):
    colors = list(map(str, input()))
    a.append(colors)

dap = 0
def width(): #가로 카운트
    global dap

    for k in range(n):
        c = 1
        for l in range(n - 1):
            if a[k][l] == a[k][l + 1]:
                c += 1
                dap = max(dap, c)
            else:
                c = 1

def height(): #세로 카운트
    for k in range(n):
        global dap
        c = 1
        for l in range(n - 1):
            if a[l][k] == a[l + 1][k]:
                c += 1
                dap = max(dap, c)
            else:
                c = 1


for i in range(n):
    for j in range(n - 1):
        if a[i][j] != a[i][j + 1]:
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            width()
            height()
            a[i][j + 1], a[i][j] = a[i][j], a[i][j + 1]
        if a[j][i] != a[j + 1][i]:
            a[j][i], a[j + 1][i] = a[j + 1][i], a[j][i]
            width()
            height()
            a[j + 1][i], a[j][i] = a[j][i], a[j + 1][i]

print(dap)