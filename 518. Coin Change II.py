class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def numberOfWays(i,amount):
            if amount==0:
                return 1
            if i==len(coins):
                return 0
            if memo[i][amount]!=-1:
                return memo[i][amount]
            if coins[i]>amount:
                memo[i][amount]=numberOfWays(i+1,amount)
            else:
                memo[i][amount]=numberOfWays(i,amount-coins[i])+numberOfWays(i+1,amount)
            return memo[i][amount]
        memo=[[-1]*(amount+1) for _ in range(len(coins))]
        return numberOfWays(0,amount)
            
  ---
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=1
        for i in range(n-1,-1,-1):
            for j in range(1,amount+1):
                if coins[i]>j:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j-coins[i]]
        return dp[0][amount]
        
