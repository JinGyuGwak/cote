#삽입정렬 (특정한 데이터를 적절한 위치에 삽입 한다)
nums = [5,10,2,1,0]
for i in range(1,len(nums)):
    i2=i-1
    cNum=nums[i]

    while nums[i2]>cNum and i2>=0:
        nums[i2+1]=nums[i2]
        i2-=1
    nums[i2+1]=cNum
    print(f'nums:,{nums}')