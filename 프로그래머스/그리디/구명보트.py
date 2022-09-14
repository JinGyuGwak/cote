from collections import deque
def solution(a, limit):
    a.sort()
    people=deque(a)
    answer=0
    while(len(people)>0):
        if len(people)==1 :
            answer+=1
            break

        if people[0]+people[-1]>limit :
            people.pop()
            answer+=1
        elif people[0]+people[-1]<=limit :
            answer+=1
            people.pop()
            people.popleft()
    return answer





print(solution([40, 40, 40, 50, 60, 60, 70, 80],100))
