from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase=deque()
        decrease=deque()
        left=ans=0
        for right in range(len(nums)):
            while increase and increase[-1]>nums[right]:
                increase.pop()
            while decrease and decrease[-1]<nums[right]:
                decrease.pop()
            increase.append(nums[right])
            decrease.append(nums[right])
            while decrease[0]-increase[0]>limit:
                if decrease[0]==nums[left]:
                    decrease.popleft()
                if increase[0]==nums[left]:
                    increase.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans
                
        
