from functools import cache
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            n=len(questions)
            if i>=n:
                return 0
            j=i+questions[i][1]+1
            return max(questions[i][0]+dp(j),dp(i+1))
        return dp(0)
----
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            j=i+questions[i][1]+1
            dp[i]=max(dp[min(j,n)]+questions[i][0],dp[i+1])
        return dp[0]
        
