def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()
    count = n - len(lost)
    a=[]
    for i in range(len(lost)):
        a.append(lost[i])

    for i in a:
        if i in reserve:
            count += 1
            lost.remove(i)
            reserve.remove(i)
    for i in lost:
        if i - 1 in reserve:
            count += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            count += 1
            reserve.remove(i + 1)
    return count


solution(2, [2, 1], [1, 2])