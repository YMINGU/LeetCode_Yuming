class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        non_obstacles=0
        start_row,start_col=0,0
        for row in range(m):
            for col in range(n):
                cell=grid[row][col]
                if cell>=0:
                    non_obstacles+=1
                if cell==1:
                    start_row,start_col=row,col
        path_count=0
        def backtrack(row,col,remain):
            nonlocal path_count
            if grid[row][col]==2 and remain==1:
                path_count+=1
                return
            temp=grid[row][col]
            remain-=1
            grid[row][col]=-4
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                next_row,next_col=row+dy,col+dx
                if not (0<=next_row<m and 0<=next_col<n):
                    continue
                if grid[next_row][next_col]<0:
                    continue
                backtrack(next_row,next_col,remain)
            grid[row][col]=temp
        backtrack(start_row,start_col,non_obstacles)
        return path_count
        
