from functools import cache
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i,remain):
            if i==len(piles) or k==0:
                return 0
            ans=dp(i+1,remain)
            curr=0
            for j in range(min(remain,len(piles[i]))):
                curr+=piles[i][j]
                ans=max(ans,dp(i+1,remain-1-j)+curr)
            return ans
        return dp(0,k)

-----
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n=len(piles)
        dp=[[0]*(k+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for remain in range(1,k+1):
                dp[i][remain]=dp[i+1][remain]
                curr=0
                for j in range(min(len(piles[i]),remain)):
                    curr+=piles[i][j]
                    dp[i][remain]=max(dp[i][remain],curr+dp[i+1][remain-j-1])
        return dp[0][k]
        
