from collections import deque


N, M = map(int, input().split())
maze = [input() for _ in range(N)]
chk = [[False] * M for _ in range(N)]
chk[0][0] = True

q = deque()
q.append((0, 0, 1))

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M
# 범위를 벗어나는지 체크하고 벗어나지 않으면 1을 리턴
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def bfs():
    while q:
        y, x, d = q.popleft()

        if y == N - 1 and x == M - 1:
            return d # (y,x)가 도착지에 있을때의 값임

        nd = d + 1
        for k in range(4): #동남서북 값 계산
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not chk[ny][nx] and maze[ny][nx] == '1':
                # 범위 안에 있고, 아직 가지 않은 곳이며 미로에서 1인 부분일경우
                chk[ny][nx] = True
                q.append((ny, nx, nd))


print(bfs())