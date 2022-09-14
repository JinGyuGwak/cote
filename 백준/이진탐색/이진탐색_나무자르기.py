n,m=map(int,input().split()) # 4 6
a=list(map(int,input().split())) #19 15 10 17
end=max(a) # 19
start=0
result=0
while(start<=end):
    sum = 0
    mid = (start + end) // 2
    for i in a :
        if mid<i :
            sum+=i-mid
    if sum>=m :
        start=mid+1
    else:
        end=mid-1
        result=mid

print(end)




