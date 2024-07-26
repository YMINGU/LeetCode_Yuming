class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            num=nums[mid]
            if num==target:
                return mid
            elif num<target:
                left=mid+1
            else:
                right=mid-1
        return left
        
