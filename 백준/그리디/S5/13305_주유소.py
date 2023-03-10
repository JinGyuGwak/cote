n=int(input())
long=list(map(int,input().split()))
cost=list(map(int,input().split()))
way=0
don=0
for i in long :
    way+=i      # 6
don=-(cost[0]*way) #30
way-=long[0]    # 4
index=0
for i in range(1,len(cost)-1):

    if cost[index]>cost[i] :
        don += way*cost[index]
        don -= way*cost[i]
        way-=long[i]
        index=i

    else :
        way-=long[i]


print(-don)