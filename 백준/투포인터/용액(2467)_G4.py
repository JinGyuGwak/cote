n=int(input())
a=list(map(int,input().split()))
#6
#-60 -50 5 12 13 30
start=0
end=n-1
sum=0
b=[]
while(start<end):
    sum=a[start]+a[end]
    if sum > 0:
        b.append([sum,a[start],a[end]])
        end -=1
    elif sum < 0 :
        b.append([sum, a[start], a[end]])
        start+=1
    elif sum == 0:
        break
if sum == 0 :
    print(a[start], a[end])
else :
    ma=min(abs(k[0]) for k in b)
    for i in b:
        if ma==abs(i[0]) :
            print(i[1],i[2])
            break
'''
도움받음
어떻게 풀어야 할 지 감을 잡았는데 이를 식으로 옮기지 못해서 존나 헤맴

'''