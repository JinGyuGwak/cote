#그래프로도 풀 수있는데 난 일단 둘 다 못품
n,m=map(int,input().split())
answer=1  # 100 4002
while(m>1):
    if n==m:
        break
    elif m%2==0:
        m=m/2
        answer+=1
    elif m%10==1:
        m=m//10
        answer+=1
    else :
        break
if n==m : print(answer)
else : print(-1)

