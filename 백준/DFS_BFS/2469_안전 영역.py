import sys
sys.setrecursionlimit(10**8)
n=int(input())/a
a=[]
ans=[]
count=1
m=0
dx=[1,0,-1,0]
dy=[0,1,0,-1] # 동 남 서 북
for i in range(n):
    a1=list(map(int,input().split()))
    if m<max(a1) : m=max(a1)
    a.append(a1)   #502 162
def dfs(y,x,t):
    for i in range(4):
        sy=y+dy[i]
        sx=x+dx[i]
        if 0<=sy<n and 0<=sx<n and chk[sy][sx]==0 and a[sy][sx]>t :
            chk[sy][sx]=1
            dfs(sy,sx,t)
    return

for k in range(1, m + 1):
    chk = [[0] * n for _ in range(n)]
    ans.append(count)
    count=0
    for i in range(n):
        for j in range(n):
            if a[i][j]>k and chk[i][j] == 0:
                chk[i][j]=1
                dfs(i,j,k)
                count+=1
print(max(ans))