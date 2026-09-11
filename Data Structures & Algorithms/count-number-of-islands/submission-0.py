class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    n_islands += 1
                    self.floodFill(i,j, grid, n_islands)
                # print(grid[i][j], end='')
            # print()
        return n_islands - 1

    def floodFill(self, i, j, grid, n_islands):
        get = lambda a,b,c: a[b][c] if 0 <= b < len(a) and 0 <= c < len(a[b]) else None
        stack = [(i,j)]
        while (stack):
            a,b = stack.pop()
            grid[a][b] = str(n_islands)
            if get(grid,a,b+1) == '1': stack.append((a,b+1))
            if get(grid,a,b-1) == '1': stack.append((a,b-1))
            if get(grid,a+1,b) == '1': stack.append((a+1,b))
            if get(grid,a-1,b) == '1': stack.append((a-1,b))