def solution(amount, value, stomach):
    j=value.index(max(value)) # 제일높은가격 인덱스
    t= amount[j]//len(stomach)
    sum=0
    hap=0
    a=[]
    if t > 0 :
        k=min(stomach)
        if min(stomach) <t :
            for i in range (len(stomach)):
                stomach[i]-=k #모든원소에서 최솟값 만큼 뺌
                hap+=stomach[i]
                if value[i] != max(value):
                    a.append([value[i], amount[i]])
            sum=k*len(value)*max(value)
        elif min(stomach) >= t:
            for i in range (len(stomach)):
                stomach[i]-=t #모든원소에서 t만큼 뺌
                hap+=stomach[i]
                if value[i] != max(value):
                    a.append([value[i], amount[i]])
            sum = t * len(value) * max(value)

    a = sorted(a, reverse=True)
    for k in a:
        if k[1]<= hap:
            sum=sum+(k[0]*k[1])
            hap=hap-k[1]
        elif k[1]>hap:
            sum=sum+(k[0]*hap)
            break
    return sum # 총가격

print(solution(
[7, 10, 4, 5], [5, 4, 3, 1], [4, 6, 2, 8]))