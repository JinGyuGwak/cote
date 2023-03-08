import sys
sys.setrecursionlimit(10**8)
n=int(input()) # 9
v,w=map(int,input().split()) # 7 3
m=int(input()) # 7
a=[[0]*n for _ in range(n)]
count=0
visit=[0]*n
hap=[]
for _ in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=a[y-1][x-1]=1


def dfs(c,dap):
    for i in range(n):
        if a[c][i] == 1 :
            if i == w-1:
                hap.append(dap)
                return dap
            elif visit[i] == 0 :
                visit[i]=1
                dfs(i,dap+1)

    return -2

visit[v-1]=1
dfs(v-1,0)

if len(hap)>0 : print(hap[0]+1)
else : print(-1)

'''
4
1 4
3
1 2
1 3
3 4
'''