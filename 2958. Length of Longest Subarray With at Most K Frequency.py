from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0
        start=-1
        freq=Counter()
        for end in range(len(nums)):
            freq[nums[end]]+=1
            while freq[nums[end]]>k:
                start+=1
                freq[nums[start]]-=1
            ans=max(ans,end-start)
        return ans
            
        
