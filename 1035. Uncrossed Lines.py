class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        memo={}
        def solve(i,j):
            if i<=0 or j<=0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if nums1[i-1]==nums2[j-1]:
                memo[(i,j)]=1+solve(i-1,j-1)
            else:
                memo[(i,j)]=max(solve(i-1,j),solve(i,j-1))
            return memo[(i,j)]
        return solve(n1,n2)
  -----
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n1][n2]
  ----
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        dp=[0]*(n2+1)
        dp_prev=[0]*(n2+1)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[j]=dp_prev[j-1]+1
                else:
                    dp[j]=max(dp_prev[j],dp[j-1])
            dp_prev=dp[:]
        return dp[n2]
        
