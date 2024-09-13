from heapq import *
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N=len(grid)
        minH=[[grid[0][0],0,0]]
        visited=set((0,0))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while minH:
            t,r,c=heappop(minH)
            if r==N-1 and c==N-1:
                return t
            for dx,dy in directions:
                next_r,next_c=r+dy,c+dx
                if next_r<0 or next_c<0 or next_r==N or next_c==N or (next_r,next_c) in visited:
                    continue
                visited.add((next_r,next_c))
                heappush(minH,[max(t,grid[next_r][next_c]),next_r,next_c])
        
