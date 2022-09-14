n,m,k=map(int,input().split()) # 5 8 3
a=list(map(int,input().split())) # 2 4 5 4 6
a.sort(reverse=True) # 6 5 4 4 2
count=0
sum=0  ; t=0
while (count<m):
    count+=1
    if t<k :
        sum=sum+a[0]
        t+=1
    else :
        t=0
        sum=sum+a[1]

print(sum)
