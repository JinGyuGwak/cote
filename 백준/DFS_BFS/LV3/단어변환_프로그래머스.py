from collections import deque

def solution(begin, target, words):
    answer=0
    visit=[0]*len(words)
    q=deque()
    q.append([begin,0])
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer=cnt
            break
        for i in range (len(words)):
            temp=0
            if visit[i]==0:
                for j in range (len(words[i])):
                    if word[j] != words[i][j] :
                        temp+=1
                if temp == 1:
                    q.append([words[i],cnt+1])
                    visit[i]=1
    return answer
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))