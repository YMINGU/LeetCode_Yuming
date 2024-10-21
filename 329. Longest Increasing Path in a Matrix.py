class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m,n=len(matrix),len(matrix[0])
        memo=[[0]*n for _ in range(m)]
        res=0
        def dfs(i,j):
            if memo[i][j]:
                return memo[i][j]
            path=1
            for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj]>matrix[i][j]:
                    path=max(path,1+dfs(i+di,j+dj))
            memo[i][j]=path
            return path
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j))
        return res
        
