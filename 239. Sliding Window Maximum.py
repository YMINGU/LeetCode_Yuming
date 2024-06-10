from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        stack=deque()
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            if stack[0]+k==i:
                stack.popleft()
            if i>=k-1:
                ans.append(nums[stack[0]])
        return ans
                
        
