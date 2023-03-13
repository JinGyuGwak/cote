
def solution(n, a):
    count = 0
    visit=[]
    visit = [0] * n
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and i!=j and visit[i]==0:
                visit[i]=1
                visit[j]=1
                dfs(j,a,visit)
                count+=1
    for cc in visit :
        if cc == 0:
            count+=1
    print(visit)
    return count
def dfs(dap,a,visit):
    for i in range(len(a[dap])):
        if a[dap][i] ==1 and visit[i] == 0 :
            visit[i]=1
            dfs(i,a,visit)
    return

#다들 visit도 같이 넘겨주네

print (solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
