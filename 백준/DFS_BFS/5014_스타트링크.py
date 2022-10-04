from collections import deque
F,S,G,U,D = map(int,input().split())
#F : 건물 높이 , S : 현재 층 , G : 가려는 층 ,U : 올라가는 층, D : 내려가는 층
# (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)
q=deque()
q.append(S)
count=0
chk=[0]*(1_000_001)
sw=0
if S>G and D==0 :
    sw=1
    print("use the stairs")
elif S<G and U==0:
    sw=1
    print("use the stairs")


while q:
    if sw==1:
        break
    t=len(q)
    count+=1
    for i in range(t):
        a=q.popleft()
        if a==G :
            print(count-1)
            sw=1
            break
        if a+U<=F and chk[a+U]==0 :
            chk[a+U] = 1
            q.append(a+U)

        if a-D>0 and chk[a-D]==0:
            chk[a-D] =1
            q.append(a-D)
if sw==0:
    print("use the stairs")