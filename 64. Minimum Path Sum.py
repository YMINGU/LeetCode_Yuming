from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(row,col):
            if row+col==0:
                return grid[row][col]
            ans=float("inf")
            if row>0:
                ans=min(ans,dp(row-1,col))
            if col>0:
                ans=min(ans,dp(row,col-1))
            return grid[row][col]+ans
        m=len(grid)
        n=len(grid[0])
        return dp(m-1,n-1)
    ----
  class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[float("inf")]*(n) for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(m):
            for j in range(n):
                if i+j==0:
                    continue
                ans=float("inf")
                if i>0:
                    ans=min(ans,dp[i-1][j])
                if j>0:
                    ans=min(ans,dp[i][j-1])
                dp[i][j]=grid[i][j]+ans
        return dp[m-1][n-1]
    ----
    class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[float("inf")]*n
        dp[0]=0
        for row in range(m):
            next_row=[0]*n
            for col in range(n):
                next_row[col]=dp[col]
                if col>0:
                    next_row[col]=min(next_row[col],next_row[col-1])
                next_row[col]+=grid[row][col]
            dp=next_row
        return dp[n-1]
        
