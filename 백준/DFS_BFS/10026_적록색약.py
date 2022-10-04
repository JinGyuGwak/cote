import sys

sys.setrecursionlimit(10 ** 8)
n=int(input())
a=[list(input()) for i in range(n)]
chk=[[0]*n for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0
def dfs(y,x,color):
    global ans
    for i in range(4):
        cy=y+dy[i]
        cx=x+dx[i]
        if 0<=cy<n and 0<=cx<n and a[cy][cx] in color and chk[cy][cx]==0:
            chk[cy][cx]=1
            dfs(cy,cx,color)
for i in range(n):
    for j in range(n):
        if chk[i][j]==0:
            ans+=1
            chk[i][j]=1
            dfs(i,j,a[i][j])
print(ans,end=' ')
ans=0
chk=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if chk[i][j]==0:
            ans+=1
            chk[i][j]=1
            dfs(i,j,'B' if a[i][j]=='B' else 'RG')
print(ans)