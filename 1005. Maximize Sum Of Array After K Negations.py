from heapq import *
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapify(nums)
        while k>0:
            k-=1
            num=heappop(nums)
            heappush(nums,-num)
        return sum(nums)
        
        
