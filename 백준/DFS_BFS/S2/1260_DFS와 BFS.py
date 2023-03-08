from collections import deque
import sys
sys.setrecursionlimit(10**8)
n,m,v=map(int,input().split())
a=[[0]*n for _ in range(n)]
for _ in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
    a[y-1][x-1]=1

q=deque()
visit=[0]*n
visit[v-1]=1

dap=[v] #0

def dfs(check): #시작 값 v = 0
    for i in range(n):
        if a[check][i]==1 and visit[i]==0:
            visit[i]=1
            dap.append(i+1)
            dfs(i)
    return

def bfs(check):
    for i in range(n):
        if a[check][i]==1 and visit[i]==0:
            visit[i]=1
            q.append(i)
    if len(q)>0 :
        test=q.popleft()
        dap.append(test+1)
        bfs(test)
    return


dap=[v] #0
dfs(v-1)
for i in dap:
    print(i, end=" ")
dap.clear()

visit=[0]*n
visit[v-1]=1
dap=[v]
bfs(v-1)
print()
for i in dap:
    print(i, end=" ")
