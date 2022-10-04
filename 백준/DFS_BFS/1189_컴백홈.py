r, n, k= map(int, input().split())
chk=[[0] * n for i in range(r)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
count=0
def dfs(y,x,ans):
    global count
    if y==0 and x==(n-1):
        if ans==k-1 :
            count+=1
        return
    for t in range(4):
        sy = y + dy[t]
        sx = x + dx[t]
        if 0<=sy<r and 0<=sx<n and a[sy][sx]!='T' and chk[sy][sx]==0:
            chk[sy][sx]=1
            dfs(sy,sx,ans+1)
            chk[sy][sx] = 0
    return



a=[list(input()) for i in range(r)]
chk[r-1][0]=1
dfs(r-1,0,0)
print(count)