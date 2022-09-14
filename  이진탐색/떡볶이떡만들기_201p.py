#자르는 높이의 최대값
n,m=map(int,input().split())# 4 6
a=list(map(int,input().split())) #19 15 10 17
end=max(a)
start=0
result=0
while(start<end):
    sum=0
    mid=(start+end)//2
    for i in a:
        if i>mid:
            sum+=i-mid

    if sum<m:
        end=mid-1
    else :
        start = mid + 1
        result=mid

    print(mid)
print(result)