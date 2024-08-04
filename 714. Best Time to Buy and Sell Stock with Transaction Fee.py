from functools import cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i,holding):
            if i==len(prices):
                return 0
            ans=dp(i+1,holding)
            if holding:
                ans=max(ans,dp(i+1,False)+prices[i]-fee)
            else:
                ans=max(ans,dp(i+1,True)-prices[i])
            return ans
        return dp(0,False)
------
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[0]*2 for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for holding in range(2):
                ans=dp[i+1][holding]
                if holding:
                    ans=max(ans,dp[i+1][False]+prices[i]-fee)
                else:
                    ans=max(ans,dp[i+1][True]-prices[i])
                dp[i][holding]=ans
        return dp[0][False]
        
