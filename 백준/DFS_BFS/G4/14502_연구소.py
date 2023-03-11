import copy
import sys
from collections import deque
n,m=map(int,input().split())
a=[]
d=[[1,0],[-1,0],[0,1],[0,-1]]
for _ in range(n):
    b=list(map(int,sys.stdin.readline().split()))
    a.append(b)


result=0
def bfs():
    test=copy.deepcopy(a)
    q=deque()

    for x in range(n):
        for y in range(m):
            if test[x][y]==2:
                q.append(x)
                q.append(y)
    while q :
        r=q.popleft()
        c=q.popleft()

        for i in range(4):
            dr=r+d[i][0]
            dc=c+d[i][1]

            if (0<=dr<n) and (0<=dc<m) :

                if test[dr][dc]==0:
                    test[dr][dc]=2
                    q.append(dr)
                    q.append(dc)

    global result
    count=0
    for i in range(n):
        for j in range(m):
            if test[i][j]==0:
                count+=1
    result=max(result,count)


def wall(count):
    if count==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j]==0 :
                a[i][j]=1
                wall(count+1)
                a[i][j]=0

    return

wall(0)
print(result)