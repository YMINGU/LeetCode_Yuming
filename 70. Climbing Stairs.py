class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i==1:
                return 1
            if i==2:
                return 2
            if i in memo:
                return memo[i]
            memo[i]=dp(i-1)+dp(i-2)
            return memo[i]
        memo={}
        return dp(n)
-----
from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i==1:
                return 1
            if i==2:
                return 2
            return dp(i-1)+dp(i-2)
        return dp(n)
  ------
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
