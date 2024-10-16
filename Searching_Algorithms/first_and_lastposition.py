#Solved in 41:38 minutes
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start: int=0
        end: int=len(nums)-1
        starttarget,endtarget=-1,-1
        if(len(nums)==0):
            return [starttarget,endtarget]
        while(start<=end):
            mid: int=(start+end)//2
            if(target>nums[mid]):
                start=mid+1
            elif(target<nums[mid]):
                end=mid-1
            elif(target==nums[mid]):
                starttarget: int=mid-1
                while(starttarget!=-1 and target==nums[starttarget]):
                    starttarget-=1
                starttarget+=1
                endtarget: int=mid+1
                while(endtarget!=len(nums) and target==nums[endtarget]):
                    endtarget+=1
                endtarget-=1
                break
        return [starttarget,endtarget]

class main():
    s=Solution()
    print(s.searchRange([2,2],3))

if(__name__=="__main__"):
    main()


    '''
    LeetCode Solution
    class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]'''