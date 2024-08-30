from collections import defaultdict
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        seen=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def bfs(row,col):
            area=1
            sol=True
            queue=deque([(row,col)])
            seen.add((row,col))
            while queue:
                row,col=queue.popleft()
                for dx,dy in directions:
                    next_row,next_col=row+dy,col+dx
                    if not 0<=next_row<m or not 0<=next_col<n:
                        sol=False
                    elif grid[next_row][next_col]==1 and (next_row,next_col) not in seen:
                        area+=1
                        queue.append((next_row,next_col))
                        seen.add((next_row,next_col))
            return (area,sol)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in seen:
                    a,b=bfs(i,j)
                    if b:
                        count+=a
        return count
                
        
