from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for c in count.keys():
            if count[c]>=2:
                return True
        return False
  ----
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=set()
        for num in nums:
            if num in count:
                return True
            count.add(num)
        return False
        
