#내가 못품
k,n=map(int,input().split())
a=[]
for i in range(k):
    a1=int(input())
    a.append(a1)
start=1 # ㅋㅋ ㅅ..ㅂ..
end=max(a)
while(start<=end):
    mid=(start+end)//2
    sum=0

    for i in a:
        sum+=i//mid
    if sum>=n:
        start=mid+1
    else :
        end=mid-1

print(end)

