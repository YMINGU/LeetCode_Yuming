class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0 or nums is None:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(self.rob_simple(nums[:-1]),self.rob_simple(nums[1:]))
    def rob_simple(self,nums):
        t1=0
        t2=0
        for curr in nums:
            temp=t1
            t1=max(curr+t2,t1)
            t2=temp
        return t1
        
