from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for xi,yi in points:
            dist=xi**2+yi**2
            heappush(heap,(-dist,(xi,yi)))
            if len(heap)>k:
                heappop(heap)
        return [pair[1] for pair in heap]
        
