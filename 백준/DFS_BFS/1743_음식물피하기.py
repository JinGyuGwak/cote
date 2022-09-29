import sys
sys.setrecursionlimit(10**8)
n,m,k=map(int,input().split())
a=[[0] * m for _ in range(n)]
chk=[[0]* m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1] #돟 남 북 서
re=[]
ans=[]
for i in range(k):
    a1,a2=map(int,input().split())
    a[a1 - 1][a2 - 1]=1
size=1

def bfs(y,x,ct):
    global size
    for t in range(4):
        sy=y+dy[t]
        sx=x+dx[t]
        if 0<= sy <n and 0<= sx <m and a[sy][sx]!=0 and a[sy][sx]==1 and chk[sy][sx]==0:
            size+=1
            a[sy][sx]=size
            chk[sy][sx]=1
            bfs(sy,sx,size)
    return

for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            chk[i][j]=1
            bfs(i,j,size)
            re.append(size)
            size=1
if len(re):
    print(max(re))
else : print(0)