n=int(input())
a=[]
for _ in range(n):
    x=int(input())
    a.append(x)

a.sort()
long=len(a)
dap=a[long-1]
c=0
for i in range(long):
    if a[i]*(long-c)>dap:
        dap=a[i]*(long-c)
    c+=1

print(dap)





