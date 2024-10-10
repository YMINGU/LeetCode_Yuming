class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        if n==0:
            ans.append([lower,upper])
            return ans
        if lower<nums[0]:
            ans.append([lower,nums[0]-1])
        for i in range(n-1):
            if nums[i+1]-nums[i]<=1:
                continue
            ans.append([nums[i]+1,nums[i+1]-1])
        if upper>nums[n-1]:
            ans.append([nums[n-1]+1,upper])
        return ans
                
            
        
