class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        ans=nums[0]
        for num in nums[1:]:
            curr=max(num,curr+num)
            ans=max(ans,curr)
        return ans
        
