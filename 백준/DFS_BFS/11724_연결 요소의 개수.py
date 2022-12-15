import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m = map(int, input().split())
adj = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: x - 1, map(int, input().split()))  # 0-based
    adj[u][v] = adj[v][u] = 1

chk=[False]*n
ans=0

def dfs(now):
    for nxt in range(n):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt]=True
            dfs(nxt)

for i in range(n):
    if not chk[i]:
        chk[i]=True
        ans += 1
        dfs(i)

print(ans)




