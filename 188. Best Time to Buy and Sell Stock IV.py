from functools import cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i,holding,remain):
            if i==len(prices) or remain==0:
                return 0
            ans=dp(i+1,holding,remain)
            if holding:
                ans=max(ans,prices[i]+dp(i+1,False,remain-1))
            else:
                ans=max(ans,-prices[i]+dp(i+1,True,remain))
            return ans
        return dp(0,False,k)
  ----
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for remain in range(1,k+1):
                for holding in range(2):
                    ans=dp[i+1][holding][remain]
                    if holding:
                        ans=max(ans,dp[i+1][0][remain-1]+prices[i])
                    else:
                        ans=max(ans,dp[i+1][1][remain]-prices[i])
                    dp[i][holding][remain] = ans
        return dp[0][0][k]
        
