from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums:
            heappush(heap,num)
            if len(heap)>k:
                heappop(heap)
        return heap[0]
            
  ----
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while len(nums)>k:
            heappop(nums)
        return nums[0]
        
