from collections import deque
def solution(arr, k):
    answer = []
    a=deque()
    ma=0
    for i in range(k):
        a.append(arr[i])
        if ma<arr[i] : ma=arr[i]
    answer.append(ma)
    for j in range(k,len(arr)):
        a.append(arr[j])
        a.popleft()
        answer.append(max(a))

    return answer


print(solution([4, 2, 6, 4, 2, 3], 3))