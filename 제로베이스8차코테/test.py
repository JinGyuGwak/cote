def dfs(x, current):
    current += a[x][2]
    if a[x][1] > ls:
        cou.append(current)
    for i in range(x+1, len(a)):
        if a[x][1] > a[i][0]:
            continue
        dfs(i, current)

def solution(start, end, price):
    for i in range(len(start)):
        a.append([start[i],end[i],price[i]])
    a.sort()
    ls=max([s for s,e,p in a])
    for i in range(len(start)):
        dfs(i,0)
    return max(cou)
meetings = []
a=[]
cou=[]
ls=0
print(solution([1, 5, 10, 6, 5], [5, 6, 12, 9, 12], [10, 40, 30, 20, 50]))