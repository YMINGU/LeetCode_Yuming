from heapq import *
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for x,y,z in times:
            graph[x-1].append([y-1,z])
        distances=[inf]*n
        distances[k-1]=0
        heap=[(0,k-1)]
        while heap:
            curr,node=heappop(heap)
            if curr>distances[node]:
                continue
            for neigh,weight in graph[node]:
                dist=curr+weight
                if distances[neigh]>dist:
                    distances[neigh]=dist
                    heappush(heap,(dist,neigh))
        ans=max(distances)
        return ans if ans<inf else -1
        
