from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ans=-1
        counts=defaultdict(int)
        for num in nums:
            counts[num]+=1
        for key in counts:
            if counts[key]==1:
                ans=max(ans,key)
        return ans
------------------------------------------------------------------
