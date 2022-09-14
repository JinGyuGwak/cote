#시발 이분탐색 아니네
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()
for i in b:  # b는 타겟임
    start = 0;
    last = n-1
    count=0
    sw=0
    while (start <= last):
        mid = (start + last) // 2
        if a[mid] < i:
            start=mid+1
        elif a[mid]>i:
            last=mid-1
        else:
            count += 1
            for j in range(mid+1,n):
                if a[j]==i:
                    count+=1
                else : break
            for k in range(mid-1,-1,-1):
                if a[k]==i:
                    count+=1
                else : break
            print(count, end=' ')
            sw=1
            break
    if sw==0 :
        print(count, end=' ')



