n,k=map(int,input().split()) # 25 5
c=0
while (1<n):
    if n%k==0:
        n=n/k
        c+=1
    else :
        n-=1
        c+=1
print(c)






