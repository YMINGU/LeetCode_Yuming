from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue=deque()
        m=len(grid)
        n=len(grid[0])
        fresh=0
        for row in range(m):
            for col in range(n):
                if grid[row][col]==2:
                    queue.append((row,col))
                elif grid[row][col]==1:
                    fresh+=1
        queue.append((-1,-1))
        minutes=-1
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            row,col=queue.popleft()
            if row==-1:
                minutes+=1
                if queue:
                    queue.append((-1,-1))
            else:
                for dx,dy in directions:
                    next_row,next_col=row+dy,col+dx
                    if 0<=next_row<m and 0<=next_col<n:
                        if grid[next_row][next_col]==1:
                            grid[next_row][next_col]=2
                            fresh-=1
                            queue.append((next_row,next_col))
        return minutes if fresh==0 else -1
        
        
