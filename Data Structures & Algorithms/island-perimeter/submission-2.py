class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1

            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1

            per = 0
            for dr,dc in directions:
                per += dfs(r+dr,c+dc)

            return per

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r,c)