class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]:
                if i!=j:
                    nums[j]=nums[i]
                    nums[i]=0
                j+=1
-----
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums
        
