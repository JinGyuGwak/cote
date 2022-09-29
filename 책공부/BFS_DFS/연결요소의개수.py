'''
# N*M 크기의 2차원 배열
n = 5
m = 2
arr = [[0]*m for _ in range(n)]

# [[0,0],[0,0],[0,0],[0,0],[0,0]]


만일, 아래와 같이 배열을 초기화 한다면 값을 하나 변경했을 때 의도하지 않은 것까지 변경될 수 있다.

# N*M 크기의 2차원 배열
n = 5
m = 2
arr = [[0]*m]*n
arr[0][0] = 5

# [[5,0],[5,0],[5,0],[5,0],[5,0]]
'''

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().split())  #6 5
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, input().split()))  # 0-based
    adj[u][v] = adj[v][u] = 1

chk = [False] * N #chk 는 방문 체크 배열 (1차원 배열)
# adj 는 그래프임
ans = 0
#여기까지가 입력

def dfs(now):
    for i in range(N):
        if adj[now][i] and not chk[i]: #chk가 0이고 adj가 1일 때
            #0번에서 갈 수 있는 모든 루트를 계산함
            chk[i] = True
            dfs(i)

for i in range(N):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)
print(ans)