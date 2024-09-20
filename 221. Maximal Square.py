class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0]) if rows else 0
        dp=[[0]*(cols+1) for _ in range(rows+1)]
        maxsqlen=0
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(min(dp[i][j-1],dp[i-1][j]),dp[i-1][j-1])+1
                    maxsqlen=max(maxsqlen,dp[i][j])
        return maxsqlen**2
  -----
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0]) if rows else 0
        dp=[0]*(cols+1)
        maxsqlen=0
        prev=0
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                temp=dp[j]
                if matrix[i-1][j-1]=="1":
                    dp[j]=min(min(dp[j-1],prev),dp[j])+1
                    maxsqlen=max(maxsqlen,dp[j])
                else:
                    dp[j]=0
                prev=temp
        return maxsqlen**2
