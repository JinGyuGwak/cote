from sys import stdin
import heapq
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

def bfs(z, x, y):
    queue = []
    heapq.heappush(queue, [0, z, x, y])
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]  # 건물 내 각 위치를 방문했는지 확인할 수 있는 3차원 배열 생성
    visited[z][x][y] = True  # 시작 위치를 방문한 것으로 처리


    while queue:
        cnt, cz, cx, cy = heapq.heappop(queue)  # 현재 위치 정보 pop

		# 현재 위치와 출구 위치가 같은 경우
        if cz == ez and cx == ex and cy == ey:
            return cnt  # 현재 위치(출구 위치)까지 이동하는데 걸린 시간 반환

		# 상하동서남북 위치로 이동하면서
        for d in range(6):
            nz = cz + dz[d]
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:  # 다음 위치가 건물 내 있고
                if building[nz][nx][ny] != '#' and not visited[nz][nx][ny]:  # 다음 위치로 이동할 수 있으면서 아직 이동하지 않은 경우
                    heapq.heappush(queue, [cnt + 1, nz, nx, ny])  # [다음 위치까지 이동하는데 걸리는 시간(현재 위치까지 이동하는데 걸린 시간 + 1), 다음 위치 z, 다음 위치 x, 다음 위치 y] 데이터 우선순위 큐에 저장
                    visited[nz][nx][ny] = True  # 다음 위치를 방문한 것으로 표시

    return 0  # 출구를 찾지 못한 채 더 이상 이동할 칸이 없는 경우 0 반환


while True:
    l, r, c = map(int, stdin.readline().split())

	# 주어진 값이 모두 0인 경우 종료
    if l == r == c == 0:
        break

    sx = 0
    sy = 0
    sz = 0

    ex = 0
    ey = 0
    ez = 0

	# 빌딩 정보를 3차원 배열에 저장
    building = [[] * r for _ in range(l)]
    for i in range(l):
        for j in range(r):
            tmp = list(map(str, stdin.readline().strip()))
            # 시작 위치가 주어진 경우
            if 'S' in tmp:
                sz = i
                sx = j
                sy = tmp.index('S')
            # 출구 위치가 주어진 경우
            elif 'E' in tmp:
                ez = i
                ex = j
                ey = tmp.index('E')
            building[i].append(tmp)
        stdin.readline()

    result = bfs(sz, sx, sy)  # 출구까지 걸리는 시간 구하기
    if result == 0:
        print("Trapped!")
    else:
        print("Escaped in", result, "minute(s).")