class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        stack=[]
        for num in nums:
            while stack and num<stack[-1]:
                stack.pop()
            stack.append(num)
            ans+=len(stack)
        return ans
        
