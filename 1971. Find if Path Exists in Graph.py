from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen=[False]*n
        def dfs(node):
            if node==destination:
                return True
            if not seen[node]:
                seen[node]=True
                for next_node in graph[node]:
                    if dfs(next_node):
                        return True
            return False
        return dfs(source)
            
        
        
        
