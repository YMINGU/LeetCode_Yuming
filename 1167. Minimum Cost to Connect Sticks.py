from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost=0
        while len(sticks)>1:
            x=heappop(sticks)
            y=heappop(sticks)
            cost+=x+y
            heappush(sticks,x+y)
        return cost
        
