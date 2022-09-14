def solution(a):
    answer = [0] * 100000
    b=0
    for i in a:
        answer[i]+=1
        if answer[i] > len(a)//2 :
            b=answer[i]
            break
    if b!=0:
        b=max(answer)

    c=answer.index(b)
    return c

print(solution([1, 2, 2, 2, 2, 3, 2, 2, 1]))


#1000