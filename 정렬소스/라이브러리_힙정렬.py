#힙정렬
import heapq
nums=[45,2,1,54,9]
a=[]
b=[]
for i in range (len(nums)):
    heapq.heappush(a,nums[i])
for i in range(len(a)):
    b.append(heapq.heappop(a))
print(b)



