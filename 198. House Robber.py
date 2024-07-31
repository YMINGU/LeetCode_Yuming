class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==None:
            return 0
        max_amount=[None for _ in range(len(nums)+1)]
        n=len(nums)
        max_amount[n]=0
        max_amount[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            max_amount[i]=max(max_amount[i+1],max_amount[i+2]+nums[i])
        return max_amount[0]
  -----
class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==None:
            return 0
        n=len(nums)
        rob_next_next=0
        rob_next=nums[n-1]
        for i in range(n-2,-1,-1):
            curr=max(rob_next,rob_next_next+nums[i])
            rob_next_next=rob_next
            rob_next=curr
        return rob_next
        
        
