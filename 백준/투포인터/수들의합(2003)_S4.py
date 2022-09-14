n,m= map(int,input().split())
a=list(map(int,input().split()))
end=0
count =0
sum=0
for i in range(n):
    while sum<m and end<n:
        sum+=a[end]
        end+=1
    if sum == m:
        count+=1
    sum-=a[i]
print(count)
