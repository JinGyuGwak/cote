'''
그래프 탐색
너비 우선 탐색
깊이 우선 탐색
'''
import sys
sys.setrecursionlimit(10**6)
T = int(input())
ax=[1,0,-1,0] #남 동 북 서
ay=[0,1,0,-1]

#m=가로, n=세로
def dfs(x,y): #0 4
    visit[y][x]=1
    for i in range(4) :
        if x+ax[i]<m and y+ay[i]<n :
            if x+ax[i]>=0 and y+ay[i]>=0 :
                if a[y+ay[i]][x+ax[i]] == 1 and visit[y+ay[i]][x+ax[i]] ==0 :
                    dfs(x+ax[i],y+ay[i])
    return

for su in range(T):
    count=0
    m,n,k=map(int,input().split())
    a=[[0]*m for _ in range(n)]
    visit=[[0]*m for _ in range(n)]
    for _ in range(k):
        ix,iy=map(int,input().split())
        a[iy][ix]=1

    for ci in range(n): #5
        for cj in range(m): #3
            if a[ci][cj]==1 and visit[ci][cj]==0:
                count+=1
                dfs(cj,ci)

    print(count)

