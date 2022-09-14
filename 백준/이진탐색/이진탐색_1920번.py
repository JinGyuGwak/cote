def search(array,target,start,end):
    mid=(start+end)//2 #2
    if start>end : #1 2 3 4 5
        return 0
    if array[mid]>target:
        return search(array,target,start,mid-1)
    elif array[mid]<target:
        return search(array,target,mid+1,end)
    elif array[mid]==target: return 1



n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
for i in b:
    print(search(a, i, 0, len(a)-1))
