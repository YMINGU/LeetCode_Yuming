from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row,col):
            return 0<=row<m and 0<=col<n and maze[row][col]=="."
        m=len(maze)
        n=len(maze[0])
        start_row,start_col=entrance
        maze[start_row][start_col]="+"
        queue=deque([(start_row,start_col,0)])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            row,col,steps=queue.popleft()
            for dx,dy in directions:
                next_row,next_col=row+dy,col+dx
                if valid(next_row,next_col):
                    if next_row==0 or next_row==m-1 or next_col==0 or next_col==n-1:
                        return steps+1
                    maze[next_row][next_col]="+"
                    queue.append((next_row,next_col,steps+1))
        return -1
        
        
