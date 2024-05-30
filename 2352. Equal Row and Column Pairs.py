from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic=defaultdict(int)
        dic2=defaultdict(int)
        ans=0
        for row in grid:
            dic[tuple(row)]+=1
        for col in range(len(grid[0])):
            current_col=[]
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            dic2[tuple(current_col)]+=1
        for arr in dic:
            if arr in dic2:
                ans+=dic[arr]*dic2[arr]
        return ans
            
------------------------------------------------------
