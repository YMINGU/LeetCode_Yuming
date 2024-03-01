class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=0
        temp=0
        while i<len(nums):
            if nums[i]<=0:
                i+=1
        while j<len(nums):
            temp=nums[j]
            nums[j]=nums[i]**2
            nums[i]=nums[j]
            j+=1
        
        
            
        
