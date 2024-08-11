from heapq import *
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heappush(nums,heappop(nums)+1)
        MOD=10**9+7
        ans=1
        for x in nums:
            ans=(ans*x)%MOD
        return ans
        
        
