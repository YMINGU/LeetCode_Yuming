class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        INF = float('inf')
        last_day_pass = [[INF] * n for _ in range(m)]
        q = deque()
        visited = set()        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if grid[i][j] == 1:
                        q.append((i, j))
                    visited.add((i, j))
                    last_day_pass[i][j] = -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            x, y = q.popleft()
            for d0, d1 in dirs:
                if not 0 <= x+d0 < m or not 0 <= y+d1 < n or (x+d0, y+d1) in visited:
                    continue
                visited.add((x+d0, y+d1))
                last_day_pass[x+d0][y+d1] = last_day_pass[x][y] + 1
                q.append((x+d0, y+d1))

        heap = [(-last_day_pass[m-1][n-1]-1, m-1, n-1)]
        visited = set()
        while heap:
            last_day, x, y = heapq.heappop(heap)
            if x == 0 and y == 0:
                if -last_day < 0:
                    return -1              
                return -last_day if -last_day != INF else 10 ** 9
            for d0, d1 in dirs:
                if not 0 <= x+d0 < m or not 0 <= y+d1 < n or grid[x+d0][y+d1] > 0 or (x+d0, y+d1) in visited:
                    continue
                visited.add((x+d0, y+d1))
                heapq.heappush(heap, (max(last_day+1, -last_day_pass[x+d0][y+d1]), x+d0, y+d1))
        return -1
        
