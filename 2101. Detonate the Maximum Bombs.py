from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(bombs)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                xi,yi,ri=bombs[i]
                xj,yj, _=bombs[j]
                if ri**2>=(xi-xj)**2+(yi-yj)**2:
                    graph[i].append(j)
        def dfs(node,seen):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor,seen)
            return len(seen)
        ans=0
        for i in range(n):
            seen=set()
            ans=max(ans,dfs(i,seen))
        return ans
--------
from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                xi,yi,ri=bombs[i]
                xj,yj, _=bombs[j]
                if ri**2>=(xi-xj)**2+(yi-yj)**2:
                    graph[i].append(j)
        def dfs(node,seen):
            stack=[i]
            seen={i}
            while stack:
                node=stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            return len(seen)
        ans=0
        for i in range(n):
            seen=set()
            ans=max(ans,dfs(i,seen))
        return ans
--------
from collections import defaultdict
from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph=defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                xi,yi,ri=bombs[i]
                xj,yj, _=bombs[j]
                if ri**2>=(xi-xj)**2+(yi-yj)**2:
                    graph[i].append(j)
        def bfs(i):
            queue=deque([i])
            seen={i}
            while queue:
                node=queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            return len(seen)
        ans=0
        for i in range(n):
            seen=set()
            ans=max(ans,bfs(i))
        return ans
        
