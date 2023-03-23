import heapq


def solution(n, k, enemy):
    b = []
    count = 0
    for i in enemy:
        count += 1
        if len(b) != k:
            heapq.heappush(b, i)
            continue
        if b[0] < i:
            n -= heapq.heappop(b)
            heapq.heappush(b, i)
        else : n -= i

        if n < 0:
            count -= 1
            break
    return count





