class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr=0
        index={}
        res=0
        j=0
        for i in range(len(nums)):
            curr+=nums[i]
            while nums[i] in index and j<index[nums[i]]+1:
                curr-=nums[j]
                j+=1
            index[nums[i]]=i
            res=max(res,curr)
        return res
        
