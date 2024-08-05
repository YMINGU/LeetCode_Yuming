from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        @cache
        def dp(row,col):
            if row>=n or row<0 or col>=n or col<0:
                return float("inf")
            if row==n-1:
                return matrix[row][col]
            return matrix[row][col]+min(dp(row+1,col-1),dp(row+1,col),dp(row+1,col+1))
        ans=float("inf")
        for i in range(n):
            ans=min(ans,dp(0,i))
        return ans
  ---
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row=matrix[-1]
        n=len(matrix)
        for i in range(n-2,-1,-1):
            next_row=matrix[i]
            for j in range(n):
                val=row[j]
                if 0<=j-1<n:
                    val=min(val,row[j-1])
                if 0<=j+1<n:
                    val=min(val,row[j+1])
                next_row[j]+=val
            row=next_row
        return min(row)
        
