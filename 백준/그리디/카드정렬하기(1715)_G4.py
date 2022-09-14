import heapq
from sys import stdin
cards = []
result = 0
for i in range(int(stdin.readline())):
    heapq.heappush(cards, int(stdin.readline())) #cards 힙 선언
if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        result += plus
        heapq.heappush(cards, plus)

    print(result)
'''
deque 쓰다가 ㅈㄴ 복잡함
heapq 쓰면 지 혼자 정렬하기 때문에 편함
'''