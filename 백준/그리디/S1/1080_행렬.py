n,m= map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(list(map(int,input())))
for _ in range(n):
    b.append(list(map(int,input())))

def reverse(x,y):
    for k in range(x,x+3):
        for t in range(y,y+3):
            if a[k][t] == 1 : a[k][t]=0
            else : a[k][t]=1


result=0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            result+=1
            reverse(i,j)

if a==b : print(result)
else : print(-1)