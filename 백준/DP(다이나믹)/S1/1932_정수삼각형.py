n= int(input())
a=[]
d=[]
for _ in range(n):
    x=list(map(int,input().split()))
    a.append(x)

for i in range(1,n):

    for j in range(len(a[i])):
        if j==0:
            a[i][j] = a[i][j]+a[i-1][j]
        elif j==len(a[i])-1 :
            a[i][j]=a[i][j] + a[i-1][j-1]
        else :
            a[i][j]=max(a[i][j]+a[i-1][j-1],a[i][j]+a[i-1][j])

print(max(a[n-1]))