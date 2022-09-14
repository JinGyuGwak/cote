n,m=map(int,input().split())
a=[]
mi=[]
for i in range (n):
    al=list(map(int,input().split()))
    a.append(al)
for i in a:
    mi.append(min(i))
print(max(mi))