from collections import defaultdict
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph=defaultdict(list)
        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)
        ans=0
        for node1 in range(n):
            for node2 in range(node1+1,n):
                curr=len(graph[node1])+len(graph[node2])
                if node2 in graph[node1]:
                    curr-=1
                ans=max(ans,curr)
        return ans
        
        
