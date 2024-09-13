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
    -----
from collections import deque
class Solution(object):
    def canCross(self,m,n,cells,day):
        grid=[[0]*n for _ in range(m)]
        queue=deque()
        for r,c in cells[:day]:
            grid[r-1][c-1]=1
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]!=0:
                return False
            if r==m-1:
                return True
            grid[r][c]=-1
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                if dfs(r+dr,c+dc):
                    return True
            return False
        for i in range(n):
            if grid[0][i]==0 and dfs(0,i):
                return True
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
        
        
