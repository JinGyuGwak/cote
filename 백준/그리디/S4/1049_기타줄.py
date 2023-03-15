n,m=map(int,input().split()) #n개 끊어짐
a=[]
b=[]
for _ in range(m):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
result=0

six= min(a)
one= min(b)


if one*6 <= six :
    result=one*n
    n=0


while n>=6 :
    n-=6
    result+=six

if one*n > six : result+=six
else : result+=one*n

print(result)

