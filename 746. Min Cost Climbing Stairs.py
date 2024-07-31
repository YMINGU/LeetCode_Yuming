class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i<=1:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=min(dp(i-1)+cost[i-1],dp(i-2)+cost[i-2])
            return memo[i]
        memo={}
        return dp(len(cost))
        
