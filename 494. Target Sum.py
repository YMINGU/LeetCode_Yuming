class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum=sum(nums)
        if total_sum+target<0 or (total_sum+target)%2==1:
            return 0
        subset_sum=(total_sum+target)//2
        dp=[0]*(subset_sum+1)
        dp[0]=1
        for num in nums:
            for j in range(subset_sum,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[subset_sum]
        