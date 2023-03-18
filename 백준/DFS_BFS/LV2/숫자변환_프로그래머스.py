#https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque


def solution(x, y, n):
    check = [0] * 1000001
    answer = 0
    q = deque()
    q.append(x)
    while q:
        answer += 1
        for i in range(len(q)):
            t = q.popleft()
            if t == y:
                return answer
            else:
                f1 = t + n
                f2 = t * 2
                f3 = t * 3
                if f1 <= y and check[f1] == 0:
                    q.append(f1)
                    check[f1]=1
                if f2 <= y and check[f2] == 0:
                    q.append(f2)
                    check[f2]=1

                if f3 <= y and check[f3] == 0:
                    q.append(f3)
                    check[f3]=1

    return answer



solution(10,40,5)