def solution(number, k):
    q = []
    for i in number:
        while q and q[-1] < i and k > 0:
            k -= 1
            q.pop()
        q.append(i)
    if k > 0:
        return "".join(q[0:-k])

    else:
        return "".join(q)


print(solution("19876534",4))
#1924