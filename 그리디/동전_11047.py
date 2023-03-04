n,m=map(int,input().split())
a=[]
for i in range(n):
    aa=int(input())
    a.append(aa)

c=0
while 1 :
    check = a.pop()
    while check <= m :
        cc=m//check
        m=m-(cc*check)
        c=c+cc
    if m<=0 : break

print(c)

