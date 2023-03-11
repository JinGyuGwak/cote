from collections import deque
def solution(numbers, target):
    dap = []
    q = deque()
    for i in numbers :
        q.append(i)
    te=q.popleft()
    dap.append([te,-te])
    count = 0
    for i in range(1,len(numbers)):
        te=q.popleft()
        test=[]
        for j in dap[i-1]:
            test.append(j+te)
            test.append(j-te)
        dap.append(test)


    for i in dap[len(numbers)-1]:
        if i == target :
            count+=1

    return count
solution([1,1,1,1,1],3)
# 30분걸림