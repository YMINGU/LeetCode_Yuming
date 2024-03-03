class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        ans=0
        for i in range(len(nums)-1):
            left=prefix[i]
            right=prefix[-1]-prefix[i]
            if left>=right:
                ans+=1
        return ans
        
