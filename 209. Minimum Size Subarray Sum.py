class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum_window=0
        res=float('inf')
        for right in range(len(nums)):
            sum_window+=nums[right]
            while sum_window>=target:
                res=min(res,right-left+1)
                sum_window-=nums[left]
                left+=1
        return res if res!=float('inf') else 0
        
