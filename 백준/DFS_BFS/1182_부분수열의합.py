n, s = map(int,input().split())
n_list = list(map(int,input().split()))

cnt = 0

def dfs(num,sum): #sum 은 합계임
    global cnt
    if num >= n:  #리스트는 0부터 시작하기 때문에 <= 표시 씀
        return
    sum+=n_list[num]
    if sum==s:
        cnt+=1

    dfs(num+1,sum)
    dfs(num+1,sum-n_list[num])

dfs(0,0)
print(cnt)


#          n:5  s:0
#       -7 -3 -2 5 8