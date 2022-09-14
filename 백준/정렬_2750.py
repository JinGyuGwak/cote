n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()

for i in b:

    start = 0
    end = n - 1
    sw=0
    while(start<=end):

        mid=(start+end)//2
        if a[mid]>i:
            end=mid-1
        elif a[mid]<i : start=mid+1
        else :
            print(1,end=" ")
            sw=1
            break
    if sw == 0 : print(0, end=" ")

