from collections import deque
n,k=map(int,input().split())
q=deque()
time=[0]*200002
q.append(n)
while q:
    a=q.popleft()
    if a==k:
        print(time[a])
        break
    for i in (a-1,a+1,a*2):
        if 0<=i<=200000 and time[i]==0:
            time[i]=time[a]+1
            q.append(i)



