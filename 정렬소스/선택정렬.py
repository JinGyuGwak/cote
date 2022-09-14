#선택정렬(셀렉션소트)
nums=[4,2,5,1,3]
for i in range(len(nums)-1):
    mini=i
    for j in range(i+1,len(nums)):
        if nums[mini]>nums[j]:
            mini=j
    print(nums)
    nums[i],nums[mini]=nums[mini],nums[i]

