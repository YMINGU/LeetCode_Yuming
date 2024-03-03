class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all=set()
        for i in range(len(nums)+1):
            all.add(i)
        for num in nums:
            if num not in all:
                return num
        return -1
        
