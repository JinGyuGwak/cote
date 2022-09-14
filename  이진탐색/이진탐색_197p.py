def search(array,target,start,end):
    if start>end : return "no"
    mid=(start+end)//2
    if array[mid]==target : return "yes"
    elif array[mid]>target:
        return search(array,target,start,mid-1)
    else :
        return search(array,target,mid+1,end)





n=int(input())
a=list(map(int,input().split())) #2 3 7 8 9
m=int(input())
b=list(map(int,input().split())) #5 7 9
a.sort()

for i in b:
    print(search(a,i,0,n-1),end=' ')
