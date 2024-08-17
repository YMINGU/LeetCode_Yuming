from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=0
        for key in count.keys():
            if count[key]==1:
                ans+=key
        return ans
  ----
