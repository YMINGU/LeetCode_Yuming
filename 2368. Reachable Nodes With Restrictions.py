from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors=defaultdict(list)
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        seen=[False]*n
        for node in restricted:
            seen[node]=True
        
        def dfs(node):
            self.ans+=1
            seen[node]=True
            for next_node in neighbors[node]:
                if not seen[next_node]:
                    dfs(next_node)
        self.ans=0
        dfs(0)
        return self.ans
        
----------
from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors=defaultdict(set)
        for a,b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        seen=[False]*n
        for node in restricted:
            seen[node]=True
        stack=[0]
        ans=0
        seen[0]=True
        while stack:
            node=stack.pop()
            ans+=1
            for next_node in neighbors[node]:
                if not seen[next_node]:
                    seen[next_node]=True
                    stack.append(next_node)
        return ans
        
