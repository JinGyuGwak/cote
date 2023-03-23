import heapq
import sys
n= int(input())
a=[]
b=[]
for i in range(n):
    t=list(map(int,sys.stdin.readline().split()))
    a.append(t)

a.sort()
heapq.heappush(b,a[0][1])
answer=1
for i in range(1,n):
    if b[0] <= a[i][0]:
        heapq.heappop(b)
        heapq.heappush(b,a[i][1])
    else :
        heapq.heappush(b, a[i][1])
        answer+=1
print(answer)

