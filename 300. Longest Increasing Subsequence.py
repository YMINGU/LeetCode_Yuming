from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            ans=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    ans=max(ans,dp(j)+1)
            return ans
        return max(dp(i) for i in range(len(nums)))
    ----
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        
        
