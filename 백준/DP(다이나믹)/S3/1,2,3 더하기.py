n=int(input())
a=[0]*12
a[1]=1
a[2]=2
a[3]=4

for i in range(4,12):
    a[i]=a[i-1]+a[i-2]+a[i-3]

for _ in range(n):
    dap=int(input())
    print(a[dap])

