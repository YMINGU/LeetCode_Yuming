from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        @cache
        def dp(row,col):
            if row==m-1 and col==n-1:
                return 1
            if row==m or col==n or obstacleGrid[row][col]:
                return 0
            return dp(row+1,col)+dp(row,col+1)
        return dp(0,0)
                
                
  ----
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1]:
            return 0
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1]=1
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if not obstacleGrid[row][col]:
                    dp[row][col]+=dp[row+1][col]+dp[row][col+1]
        return dp[0][0]
        
        
