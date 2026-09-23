def floodFill(label: int, x: int, y: int, grid: List[List[int]]) -> int:
    stack = [(x,y)]
    grid[x][y] = label
    size = 0
    while(stack):
        i,j = stack.pop()
        size += 1
        if i+1 < len(grid):
            if grid[i+1][j] == 1:
                grid[i+1][j] = label
                stack.append((i+1,j))
        if i > 0:
            if grid[i-1][j] == 1:
                grid[i-1][j] = label
                stack.append((i-1,j))
        if j+1 < len(grid[i]):
            if grid[i][j+1] == 1:
                grid[i][j+1] = label
                stack.append((i,j+1))
        if j > 0:
            if grid[i][j-1] == 1:
                grid[i][j-1] = label
                stack.append((i,j-1))
    return size

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # This is just floodfill
        count = 2
        max_size = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    size = floodFill(count, i,j, grid)
                    max_size = max(max_size,size)
                    count += 1
        return max_size