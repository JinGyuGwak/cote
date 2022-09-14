def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

    return 0
n,target=map(int,input().split())
array=list(map(int,input().split()))
result=binary_search(array,target,0,n-1)
if result==None:
    print(f"{target}은 존재하지 않습니다")
else : print(f"{target}은 {result+1}위치에 존재합니다.")

