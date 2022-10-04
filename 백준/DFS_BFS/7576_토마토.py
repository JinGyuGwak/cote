from collections import deque
n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)]
b=[]
q=deque()
count=1
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for i in range(m):
    for j in range(n):
        if a[i][j]==1:
            q.append(i)
            q.append(j)


while( len(q)>1 ):
    count+=1
    for j in range(len(q) // 2):
        y = q.popleft()
        x = q.popleft()
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if 0 <= ay < m and 0 <= ax < n and a[ay][ax] == 0:
                q.append(ay)
                q.append(ax)
                a[ay][ax] = count

result=max(map(max,a))-1
for i in a:
    if 0 in i:
        result=-1
        break
print(result)
