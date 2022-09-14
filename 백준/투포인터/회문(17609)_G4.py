def solution(a:list):
    start=0
    end=len(a)-1
    sw=0
    while(start<end):
        if a[start]==a[end]:
            start+=1
            end-=1
        elif a[start+1]==a[end]:
            start+=1
            sw=1
        elif a[start]==a[end-1]:
            end-=1
            sw=1
        else : return 2
    if sw==0 : return 0
    else : return 1

n=int(input())
a=[]
for i in range(n):
    a1=input()
    a.append(a1)
for i in a:
    print(solution(i))

#왜 안되는건데