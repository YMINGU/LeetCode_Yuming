from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapify(stones)
        while len(stones)>1:
            stone_1=heappop(stones)
            stone_2=heappop(stones)
            if stone_1 !=stone_2:
                heappush(stones,stone_1-stone_2)
        return -heapq.heappop(stones) if stones else 0
        
