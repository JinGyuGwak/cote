n = int(input())
cards = list(map(int, input().split(' ')))
cards.sort()

m = int(input())
targets = list(map(int, input().split(' ')))
# 10 9 -5 2 3 4 5 -10

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in targets:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')