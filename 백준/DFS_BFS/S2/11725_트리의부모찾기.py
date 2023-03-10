import sys
sys.setrecursionlimit(10**8)

n=int(input())
a=[[] for _ in range(n+1)] #10만*10만


dap=[0]*(n+1)

for _ in range(n-1):
    x,y=map(int,sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)

visit=[0]*(n+1)
visit[1]=1

def dfs(index):
    for j in a[index] :
        if visit[j] == 0 :
            visit[j]=1
            dap[j]=index
            dfs(j)
    return

dfs(1)
for da in range(2,len(dap)):
    print(dap[da])


