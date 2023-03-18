#https://school.programmers.co.kr/learn/courses/30/lessons/159993#qna
from collections import deque
def solution(a):
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]

    def bfs(iy, ix, sw):
        q = deque()
        visit = [[-1] * len(a[0]) for _ in range(len(a))]
        visit[iy][ix] = 0
        q.append([iy, ix])
        while q:
            iy, ix = q.popleft()
            for i in range(4):
                dy = iy + y[i]
                dx = ix + x[i]
                if (0 <= dy < len(a)) and (0 <= dx < len(a[0])):
                    if a[dy][dx] == 'O' and visit[dy][dx] == -1:
                        visit[dy][dx] = visit[iy][ix] + 1
                        q.append([dy, dx])
                    elif sw == 0:
                        if a[dy][dx] == 'L' and visit[dy][dx] == -1:
                            return visit[iy][ix] + 1
                        if a[dy][dx] == 'E' and visit[dy][dx] == -1:
                            visit[dy][dx] = visit[iy][ix] + 1
                            q.append([dy, dx])

                    elif sw == 1:
                        if a[dy][dx] == 'E':
                            return visit[iy][ix] + 1
                        if a[dy][dx] == 'S':
                            visit[dy][dx] = visit[iy][ix] + 1
                            q.append([dy, dx])

        return -1

    dap = [[] for _ in range(2)]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 'S':
                dap[0] = [i, j]

            if a[i][j] == 'L':
                dap[1] = [i, j]

    al = bfs(dap[0][0], dap[0][1], 0)
    ae = bfs(dap[1][0], dap[1][1], 1)
    if al > -1 and ae > -1:
        return al + ae
    else:
        return -1
