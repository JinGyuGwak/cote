n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=1)
for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else : break
sum=0
for i in range (n):
    sum+=a[i]
print(sum)
