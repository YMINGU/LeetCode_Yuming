from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i]*=-1
        heapify(piles)
        while k>0:
            x=heappop(piles)
            x=x+floor(-x/2)
            heappush(piles,x)
            k-=1
        return -sum(piles)
        
