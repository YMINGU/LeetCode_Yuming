from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for num in arr:
            heappush(heap,(-abs(num-x),-num))
        while len(heap)>k:
            heappop(heap)
        return sorted([-pair[1] for pair in heap])
            
        
