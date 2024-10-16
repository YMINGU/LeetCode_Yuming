from heapq import *
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n=len(quality)
        total_cost=float("inf")
        total_q=0
        ratio=[]
        for i in range(n):
            ratio.append((wage[i]/quality[i],quality[i]))
        ratio.sort(key=lambda x:x[0])
        workers=[]
        for i in range(n):
            heappush(workers,-ratio[i][1])
            total_q+=ratio[i][1]
            if len(workers)>k:
                total_q+=heappop(workers)
            if len(workers)==k:
                total_cost=min(total_cost,total_q*ratio[i][0])
        return total_cost
        
