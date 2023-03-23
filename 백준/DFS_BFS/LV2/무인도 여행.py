import sys
sys.setrecursionlimit(10**6)
hap = 0
def solution(maps):
    global hap
    n = len(maps)
    m = len(maps[0])
    visit = [[0] * m for _ in range(n)]
    answer = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(y, x):
        global hap
        visit[y][x] = 1
        hap += int(maps[y][x])

        for i in range(4):
            r = y + dy[i]
            c = x + dx[i]
            if 0 <= r < n and 0 <= c < m and maps[r][c] != 'X' and visit[r][c] == 0:
                dfs(r, c)

        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                dfs(i, j)
                answer.append(hap)
                hap = 0
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer
print(solution(["XXXXX","XXXXX","XXXXX"]))