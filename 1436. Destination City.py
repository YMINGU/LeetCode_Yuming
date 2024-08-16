from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph=defaultdict(str)
        for path in paths:
            graph[path[0]]=path[1]
        for dst in graph.values():
            if dst not in graph.keys():
                return dst
        return null
----
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count=set()
        for i in range(len(paths)):
            count.add(paths[i][0])
        for i in range(len(paths)):
            c=paths[i][1]
            if c not in count:
                return c
        return ""
        
