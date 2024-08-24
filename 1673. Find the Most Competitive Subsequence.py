class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack=[]
        for i,n in enumerate(nums):
            while stack and n<stack[-1] and len(nums)-i+len(stack)>k:
                stack.pop()
            stack.append(n)
        return stack[:k]
        
