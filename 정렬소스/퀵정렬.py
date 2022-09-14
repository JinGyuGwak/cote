#퀵정렬
def qSort(ns):
    if len(ns)<2:
        return ns

    midIdx=len(ns)//2
    midVal=ns[midIdx]
    smallNums=[]; sameNums=[]; bigNums=[]
    for n in ns:
        if n < midVal:
            smallNums.append(n)
        elif n==midVal:
            sameNums.append(n)
        else:
            bigNums.append(n)
    return qSort(smallNums)+sameNums+qSort(bigNums)
nums=[8,1,4,3,2,5,4,10,6,8]
print(qSort(nums))


#sorted는 리스트,집합자료형, 딕셔너리 자료형 등을 입력받아 정렬
a=[7,5,9,0,3,1,6,2,4,8]
result=sorted(a,reverse=1)
a.sort()
print(result,"\n",a)

