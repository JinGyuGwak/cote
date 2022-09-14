import sys
n=int(input())
a=list(map(int,sys.stdin.readline().split()))
m=int(input())
a.sort()
count=0
# 1 2 3 5 7 9 10 11 12
start=0
end=n-1
while(start<end):
    sum=a[start]+a[end]
    if sum>m:
        end-=1
    elif sum<m:
        start+=1
    elif sum==m :
        count+=1
        start+=1
print(count)

'''
리뷰
도움받음
정렬 후 두 값과 타겟을 비교하며 서칭하는건 알았지만  투포인터의 장점을 이용한풀이를 생각하지 못해
시간초과 남 
'''
