class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        for visited postion marked as 0
        """
        directions=[[1,0] ,[0,1] ,[-1 ,0] ,[0,-1]]
        row=len(grid)
        col=len(grid[0])
        visited=[[0]*col for _ in range(row)]
        def dfs(r ,c):
            if  r<0 or c<0 or r>=row or c>=col  or grid[r][c]==0 :
                return 1
            if visited[r][c]==1:
                return 0
            visited[r][c]=1
            s=0
            for dr , dc in directions:
                s+=dfs(r+dr , c+dc)
            return s
        totalsum=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and visited[r][c]==0:
                    totalsum+=dfs(r ,c)
        return totalsum


        