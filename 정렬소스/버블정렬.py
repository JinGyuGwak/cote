# 버블정렬
nums = [10,2,7,21,8]
length = len(nums)-1
for i in range(length):
    for j in range(length-i):
        if nums[j]>nums[j+1]:
            # temp = nums[j]
            # nums[j]=nums[j+1]
            # nums[j+1]=temp
            nums[j], nums[j+1] = nums[j+1],nums[j] #첫번째 값과 첫번째 값 바꿈,두번쨰 값과 두번째 값 바꿈
        print(nums)
    print()