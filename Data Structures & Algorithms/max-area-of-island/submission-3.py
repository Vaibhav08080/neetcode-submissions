class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):

            # Out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0

            # Water cell
            if grid[r][c] == 0:
                return 0

            # Already visited
            if visited[r][c]:
                return 0

            # Mark visited
            visited[r][c] = True

            # Current cell contributes 1 area
            area = 1

            # Explore 4 directions
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        max_area = 0

        # Traverse whole grid
        for r in range(rows):
            for c in range(cols):

                # Start DFS only from unvisited land
                if grid[r][c] == 1 and not visited[r][c]:

                    current_area = dfs(r, c)

                    max_area = max(max_area, current_area)

        return max_area