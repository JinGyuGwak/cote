from collections import deque
def solution(a):
    q=deque()
    d=[[1,0],[-1,0],[0,1],[0,-1]]
    q.append(0)
    q.append(0)

    while q:
        y=q.popleft()
        x=q.popleft()
        for i in range(4):
            dy=y+d[i][0]
            dx=x+d[i][1]
            if 0 <= dy < len(a) and 0<=dx<len(a[0]) :
                if a[dy][dx] == 1:
                    a[dy][dx]=a[y][x]+1
                    q.append(dy)
                    q.append(dx)

    if a[len(a)-1][len(a[0])-1] == 1 : print(-1)
    else : print(a[len(a)-1][len(a[0])-1])









solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])