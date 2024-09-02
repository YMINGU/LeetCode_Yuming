from heapq import *
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        heads=costs[:candidates]
        tails=costs[max(candidates,len(costs)-candidates):]
        heapify(heads)
        heapify(tails)
        answer=0
        next_head,next_tail=candidates,len(costs)-1-candidates
        for _ in range(k):
            if not tails or heads and heads[0]<=tails[0]:
                answer+=heappop(heads)
                if next_head<=next_tail:
                    heappush(heads,costs[next_head])
                    next_head+=1
            else:
                answer+=heappop(tails)
                if next_head<=next_tail:
                    heappush(tails,costs[next_tail])
                    next_tail-=1
        return answer
        
-----
from heapq import *
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        pq=[]
        for i in range(candidates):
            pq.append((costs[i],0))
        for i in range(max(candidates,len(costs)-candidates),len(costs)):
            pq.append((costs[i],1))
        heapify(pq)
        answer=0
        next_head,next_tail=candidates,len(costs)-1-candidates
        for _ in range(k):
            curr_cost,curr_id=heappop(pq)
            answer+=curr_cost
            if next_head<=next_tail:
                if curr_id==0:
                    heappush(pq,(costs[next_head],0))
                    next_head+=1
                else:
                    heappush(pq,(costs[next_tail],1))
                    next_tail-=1
        return answer
                    
