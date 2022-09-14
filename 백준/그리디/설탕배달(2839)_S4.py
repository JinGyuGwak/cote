a=int(input())  # 3과 5로 나눈다
count = 0
while (a >=3):

    if a % 5 ==0 :
        a=(a//5)
        count+=a
        a=0
    else :
        count+=1
        a-=3
if a>0 :
    print(-1)
else : print(count)

