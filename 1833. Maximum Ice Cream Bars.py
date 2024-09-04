from heapq import *
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        heapify(costs)
        ans=0
        while costs and coins>=costs[0]:
            ans+=1
            coins-=heappop(costs)
        return ans
------
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        m=len(costs)
        ans=0
        m=max(costs)
        Freq=[0]*(m+1)
        for cost in costs:
            Freq[cost]+=1
        for cost in range(1,m+1):
            if not Freq[cost]:
                continue
            if coins<cost:
                break
            count=min(Freq[cost],coins//cost)
            coins-=cost*count
            ans+=count
        return ans
        
