from collections import deque
a=[]
dx=[1,1,2,2,-1,-1,-2,-2]
dy=[2,-2,1,-1,2,-2,1,-1]
a1=0
a2=0
def bfs(c1,c2):
    q=deque()
    q.append([c1,c2])
    chk[c1][c2]=1
    while q:
        y,x=q.popleft() #
        if y==a1 and x==a2:
            return
        for i in range(8):
            cy=y+dy[i]
            cx=x+dx[i]
            if 0 <= cy < t and 0 <= cx < t and chk[cy][cx] == 0 :
                q.append([cy,cx])
                chk[cy][cx]=chk[y][x]+1
n=int(input())
for i in range(n):
    t = int(input())
    chk=[[0]*t for _ in range(t)]
    b1,b2=map(int,input().split())
    chk[b1][b2]=1
    a1, a2 = map(int, input().split())
    bfs(b1,b2)
    print(chk[a1][a2]-1)




