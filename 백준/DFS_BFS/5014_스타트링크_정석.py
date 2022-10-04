from collections import deque

INF = 987654321


def is_valid_coord(x):
    return 1 <= x <= F


def bfs():
    chk = [INF] * (F + 1)
    q = deque()
    q.append((S, 0))
    while q:
        now, t = q.popleft()

        if now == G:
            return t

        nt = t + 1
        for d in (U, -D):
            nxt = now + d
            if is_valid_coord(nxt) and nt < chk[nxt]:
                chk[nxt] = nt
                q.append((nxt, nt))

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())
print(bfs())