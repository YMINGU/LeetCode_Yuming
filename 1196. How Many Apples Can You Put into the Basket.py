class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans=0
        k=5000
        for m in weight:
            if m<=k:
                ans+=1
                k-=m
            else:
                break
        return ans
----
from heapq import *
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapify(weight)
        k=5000
        ans=0
        units=0
        while weight and units+weight[0]<=5000:
            units+=heappop(weight)
            ans+=1
        return ans
        
