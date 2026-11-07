from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since all edges are equal weight, this simplifies what
        # might've been dijkstra to bfs.
        # so one approach is to start at each treasure chest and
        # perform bfs setting the value of each cell to the minimum
        # of its current value or the bfs depth

        # where n = cells and t = treasure chest, this is O(n + n*t) which is sort of like O(n^2)
        # multi-soruce bfs avoids covering the full grid for every chest
        queue = deque([(i,j,0) for i in range(0,len(grid)) for j in range(0,len(grid[i])) if grid[i][j] == 0])
        # print(f"queue: {queue}")
        while(queue):
            i,j,depth = queue.popleft()

            # skip already covered and skip water
            if (depth > 0 and grid[i][j] != 2147483647): continue
            grid[i][j] = depth
                
            if i < len(grid) - 1: queue.append((i+1,j,depth+1))
            if i > 0: queue.append((i-1,j,depth+1))
            if j < len(grid[i]) - 1: queue.append((i,j+1,depth+1))
            if j > 0: queue.append((i,j-1,depth+1))
