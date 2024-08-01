class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
        return dp[amount] if dp[amount] !=float('inf') else -1
      ----
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i<0:
                return -1
            if i==0:
                return 0
            min_cost=float("inf")
            for coin in coins:
                res=dp(i-coin)
                if res!=-1:
                    min_cost=min(min_cost,res+1)
            return min_cost if min_cost!=float("inf") else -1
        return dp(amount)
        
