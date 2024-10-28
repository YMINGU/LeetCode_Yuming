class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        max_far=nums[0]
        min_far=nums[0]
        ans=max_far
        for i in range(1,len(nums)):
            curr=nums[i]
            temp_max=max(curr,max(max_far*curr,min_far*curr))
            min_far=min(curr,min(max_far*curr,min_far*curr))
            max_far=temp_max
            ans=max(max_far,ans)
        return ans
        
