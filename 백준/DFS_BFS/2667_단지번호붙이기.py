n=int(input())
a=[]
ans=[]
chk=[[0]*n for _ in range(n)]

c=0
count=1
dx=[1,0,-1,0]
dy=[0,1,0,-1] #동 남 서 북
for i in range(n):
    a1=input()
    a.append(a1)

def dfs(y,x):
    global count
    for i in range(4):
        sx=x+dx[i]
        sy=y+dy[i]
        if 0<=sx<n and 0<=sy<n and chk[sy][sx]==0 and a[sy][sx]=='1':
            count+=1
            chk[sy][sx]=1
            dfs(sy,sx)
    return

for i in range(n):
    for j in range(n):
        if a[i][j]=='1' and chk[i][j]==0:
            c+=1
            chk[i][j]=1
            dfs(i,j)
            ans.append(count)
            count=1
print(c)
ans.sort()
for i in ans:
    print(i)


