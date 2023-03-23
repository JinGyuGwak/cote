import heapq


def converter(string):
    """ string타입 시간을 분단위의 int값으로 반환하는 함수"""
    h, m = string.split(":")
    return int(h) * 60 + int(m)


def solution(book_time):
    b = []
    a = [[] for i in range(len(book_time))]
    for i in range(len(book_time)):
        a[i].append(converter(book_time[i][0]))
        a[i].append(converter(book_time[i][1]) + 10)

    a.sort()
    heapq.heappush(b,a[0][1])
    answer = 1
    for i in range(1,len(a)):
        if b[0] <= a[i][0]:
            heapq.heappop(b)
            heapq.heappush(b,a[i][1])
        else :
            heapq.heappush(b, a[i][1])
            answer+=1
    return answer
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))