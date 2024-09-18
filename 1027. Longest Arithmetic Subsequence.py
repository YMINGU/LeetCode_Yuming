class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp={}
        for right in range(len(nums)):
            for left in range(0,right):
                dp[(right,nums[right]-nums[left])]=dp.get((left,nums[right]-nums[left]),1)+1
        return max(dp.values())
----
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        nums.sort()
        dp=[0]*len(nums)
        for i,num in enumerate(nums):
            max_size=0
            for k in range(i):
                if nums[i]%nums[k]==0:
                    max_size=max(max_size,dp[k])
            max_size+=1
            dp[i]=max_size
        max_size,max_size_i= max([(v,i) for i,v in enumerate(dp)])
        ret=[]
        curr,tail=max_size,nums[max_size_i]
        for i in range(max_size_i,-1,-1):
            if curr==dp[i] and tail%nums[i]==0:
                ret.append(nums[i])
                curr-=1
                tail=nums[i]
        return reversed(ret)
        
