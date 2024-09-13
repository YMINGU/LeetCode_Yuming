from collections import deque
class Solution(object):
    def canCross(self,row,col,cells,day):
        grid=[[0]*col for _ in range(row)]
        queue=deque()
        for r,c in cells[:day]:
            grid[r-1][c-1]=1
        for i in range(col):
            if not grid[0][i]:
                queue.append((0,i))
                grid[0][i]=-1
        while queue:
            r,c=queue.popleft()
            if r==row-1:
                return True
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                next_row,next_col=r+dr,c+dc
                if 0<=next_row<row and 0<=next_col<col and grid[next_row][next_col]==0:
                    grid[next_row][next_col]=-1
                    queue.append((next_row,next_col))
        return False
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        left=1
        right=row*col
        while left<right:
            mid=right-(right-left)//2
            if self.canCross(row,col,cells,mid):
                left=mid
            else:
                right=mid-1
        return left
        
