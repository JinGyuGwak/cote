n=int(input())
a=list(map(int,input().split()))

answer=[-1]*n
stack=[]
for i in range(n):
    while stack and a[stack[-1]]<a[i]:
        answer[stack.pop()]=a[i]

    stack.append(i)
for i in answer:
    print(i,end=' ')