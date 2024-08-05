from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row,col):
            if row+col==0:
                return 1
            ans=0
            if row>0:
                ans+=dp(row-1,col)
            if col>0:
                ans+=dp(row,col-1)
            return ans
        return dp(m-1,n-1)
  -----
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0][0]=1
        for row in range(m):
            for col in range(n):
                if row>0:
                    dp[row][col]+=dp[row-1][col]
                if col>0:
                    dp[row][col]+=dp[row][col-1]
        return dp[m-1][n-1]
        
        
