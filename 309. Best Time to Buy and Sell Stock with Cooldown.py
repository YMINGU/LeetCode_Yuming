from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i,holding):
            if i==len(prices):
                return 0
            ans=dp(i+1,holding)
            if holding:
                ans=max(ans,dp(min(i+2,len(prices)),False)+prices[i])
            else:
                ans=max(ans,dp(i+1,True)-prices[i])
            return ans
        return dp(0,False)
------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for holding in range(2):
                ans=dp[i+1][holding]
                if holding:
                    ans=max(ans,dp[min(i+2,len(prices))][False]+prices[i])
                else:
                    ans=max(ans,dp[i+1][True]-prices[i])
                dp[i][holding]=ans
        return dp[0][False]
        
