n=int(input())
a=[0]*(n+3)
a[1]=0
a[2]=1
a[3]=1
for i in range(4,n+1):

    a[i] = a[i - 1] + 1
    if i%3 == 0 :
        a[i]= min(a[i//3] + 1,a[i])
    if i%2 == 0 :
        a[i]= min(a[i//2] + 1,a[i])

print(a[n])

