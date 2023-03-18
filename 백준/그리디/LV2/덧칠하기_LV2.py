def solution(n, m, section):
    a = [0] * (n + 1)
    answer = 0
    for s in section:
        a[s] = 1
    for i in range(len(a)):
        if a[i] == 1:
            answer += 1
            for j in range(m):
                if i + j <= n: a[i + j] = 2

    return answer