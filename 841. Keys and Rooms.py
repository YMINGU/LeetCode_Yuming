class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        seen={0}
        dfs(0)
        return len(seen)==len(rooms)
------
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack=[0]
        seen={0}
        while stack:
            node=stack.pop()
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return len(seen)==len(rooms)
                
        
