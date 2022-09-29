import sys
sys.setrecursionlimit(10**8)
n,m,k=map(int,input().split())
a=[[0] * m for _ in range(n)]
chk=[[0]* m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
re=[]
for i in range(k):
    a1,a2=map(int,input().split())
    a[a1 - 1][a2 - 1]=1
#y+dy[i] 가

def bfs(y,x,ct):

    for t in range(4):
        sy=y+dy[t]
        sx=x+dx[t]
        if 0<= sy <n and 0<= sx <m and a[sy][sx]!=0 and a[sy][sx]==1 and not chk[sy][sx]:
            chk[sy][sx] = 1
            ct+=1
            re.append(ct)
            a[sy][sx]=ct
            bfs(sy,sx,ct)
    return ct

for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            chk[i][j]=True
            bfs(i,j,1)
if k==1 :
    re.append(1)
print(max(re))