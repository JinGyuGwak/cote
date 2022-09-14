import sys
n=int(input())
a=[]
result=[]
for i in range(n):
    m=int(input())
    for j in range(m):
        b,c=map(int,sys.stdin.readline().split())
        a.append([b,c])
    a.sort()
    max=a[0][1]
    answer=1
    for i in a:
        if max>i[1]:
            max=i[1]
            answer+=1
    result.append(answer)
    a=[]
for i in result:
    print(i)
