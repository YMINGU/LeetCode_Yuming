from collections import defaultdict
from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for x,y,z in flights:
            graph[y].append([x,z])
        prices=[inf]*n
        heap=[(0,dst,k)]
        while heap:
            curr,node,remain=heappop(heap)
            if remain>=0:
                if curr<prices[node]:
                    prices[node]=curr
                for neigh,weight in graph[node]:
                    price=curr+weight
                    if price<prices[neigh]:
                        prices[neigh]=price
                        heappush(heap,(price,neigh,remain-1))
        ans=prices[src]
        return ans if ans<inf else -1
  ------
