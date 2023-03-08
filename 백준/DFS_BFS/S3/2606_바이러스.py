import sys
sys.setrecursionlimit(10**8)
n=int(input()) #7 총 컴터 수
m=int(input()) #6 연걸된 번호
a=[[0]* n for i in range(n)]
dap=set([0])
for i in range(m):
    x,y=map(int,input().split())
    a[x-1][y-1]=1
    a[y-1][x-1]=1

def boj(t):
    for i in range(n):
        if a[t][i]==1 and i not in dap:
            dap.add(i)
            boj(i)
    return

boj(0)
result=list(set(dap))
print(len(result)-1)


