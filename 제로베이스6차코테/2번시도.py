from collections import deque
def solution(amount, value, stomach):
    a=[]
    b=deque()
    sum=0
    hap=0
    for i in range (len(value)):
        a.append([value[i] ,amount[i]])
        hap+=stomach[i]
    a = sorted(a, reverse=True)
    if len(stomach)==1 :
        return a[0][1]*stomach[0]
    c=a[0][1]//len(stomach) # 가장 값 높은 고기를 인원 수 만큼 나눔
    b = deque(a)
    if c>0 :
        hap-=(c*len(stomach))
        sum+=c*len(stomach)*b[0][0]
        b.popleft()
    else :
        b.popleft()
    for i in b:
        if hap>=i[1]:
            hap-=i[1]
            sum+=i[0]*i[1]
        else :
            sum+=i[0]*hap
            break

    return sum
print(solution([7],[5],[4]))