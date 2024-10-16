def findMin(nums):
    start=0
    end=len(nums)-1
    min=nums[start]
    while(start<=end):
        mid=(start+end)//2
        if(nums[mid-1]>nums[mid]):
            min=nums[mid]
            break
        elif((mid+1)!=len(nums) and nums[mid+1]<nums[mid]):
             min=nums[mid+1]
             break
        else:
            start=mid+1
        if(start==len(nums)):
            start=0
            end=mid-1
    return min

print(findMin([11,13,15,17]))

            