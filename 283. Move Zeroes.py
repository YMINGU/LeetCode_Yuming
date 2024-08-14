class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]:
                if i!=j:
                    nums[j]=nums[i]
                    nums[i]=0
                j+=1
            
        
