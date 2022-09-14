def solution(a):
    answer = []
    count=[]
    b=min(a)
    hap=0
    for i in range(len(a)):
        if b<=a[i]:
            b=a[i]
            answer.append(i)
        else :
            if hap < answer[-1]-answer[0] :
                hap = answer[-1]-answer[0]
                count.append(answer[0])
                count.append(answer[-1])
            answer.clear()
            b=a[i]
            answer.append(i)

    answer.clear()
    if hap == 1 : return [0,0]
    return count[-2:]
print(solution(
[103, 152, 124, 165, 152, 154, 159, 160, 200, 195, 205, 206, 204, 189, 156]))