class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        def bfs(employee,time):
            maxTime=0
            q=deque([(employee,time)])
            while q:
                manager,time=q.popleft()
                maxTime=max(maxTime,time)
                if manager in graph:
                    for d in graph[manager]:
                        q.append([d,time+informTime[manager]])
            return maxTime
        graph=defaultdict(list)
        for d,manager in enumerate(manager):
            if manager==-1:
                continue
            graph[manager].append(d)
        return bfs(headID,0)
        
