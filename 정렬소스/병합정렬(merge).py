#병합정렬(merge sort)
def msort(ns):
    if len(ns)<2:
        return ns
#nums = [8,1,4,3,2,5,10,6] len(nums)=8
    midIdx=len(ns)//2
    leftNums=msort(ns[0:midIdx])
    rightNums=msort(ns[midIdx:len(ns)])

    mergenums=[]
    leftIdx=0
    rightIdx=0
    while leftIdx < len(leftNums) and rightIdx < len(rightNums):

        if leftNums[leftIdx] < rightNums[rightIdx]:
            mergenums.append(leftNums[leftIdx])
            leftIdx+=1
        else:
            mergenums.append(rightNums[rightIdx])
            rightIdx+=1
    mergenums=mergenums+leftNums[leftIdx:]
    mergenums=mergenums+rightNums[rightIdx:]

    return mergenums
nums = [8,1,4,3,2,5,10,6]
print(msort(nums))
