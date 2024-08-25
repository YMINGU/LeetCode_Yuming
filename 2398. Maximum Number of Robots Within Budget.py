from collections import deque
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        ans=0
        queue=deque()
        left=0
        prefix=0
        for i in range(len(chargeTimes)):
            while queue and queue[-1][0]<=chargeTimes[i]:
                queue.pop()
            queue.append((chargeTimes[i],i))
            prefix+=runningCosts[i]
            total=queue[0][0]+(i-left+1)*prefix
            while total>budget:
                left+=1
                if left-1>=queue[0][1]:
                    queue.popleft()
                prefix-=runningCosts[left-1]
                if queue:
                    total=queue[0][0]+(i-left+1)*prefix
                else:
                    total=0
            ans=max(ans,i-left+1)
        return ans
        
