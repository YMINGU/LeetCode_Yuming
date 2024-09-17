class Solution:
    def tribonacci(self, n: int) -> int:
        dp={0:0,1:1,2:1}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i]=dfs(i-1)+dfs(i-2)+dfs(i-3)
            return dp[i]
        return dfs(n)
-------
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            return 1 if n else 0
        dp=[0]*(n+1)
        dp[1]=dp[2]=1
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
        
