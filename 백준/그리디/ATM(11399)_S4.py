n=int(input())
a=list(map(int,input().split()))
a.sort()  # 1 2 3 3 4
sum=0
answer=0
for i in a:
    sum=sum+i
    answer+=sum

print(answer)
'''
1        
1+2   
1+2+3
1+2+3+3
1+2+3+3+4

'''