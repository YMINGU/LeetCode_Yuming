class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        stack=[]
        for right in range(n+1):
            while stack and (right==n or nums[stack[-1]]>=nums[right]):
                mid=stack.pop()
                left=-1 if not stack else stack[-1]
                ans-=nums[mid]*(mid-left)*(right-mid)
            stack.append(right)
        del(stack[:])
        for right in range(n+1):
            while stack and (right==n or nums[stack[-1]]<=nums[right]):
                mid=stack.pop()
                left=-1 if not stack else stack[-1]
                ans+=nums[mid]*(mid-left)*(right-mid)
            stack.append(right)
        return ans
                
