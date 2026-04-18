# Tabulation

class Solution:

    def minPath(self, i, j, grid, dp):
        if i==0 and j==0:
            return grid[0][0]
        if i<0 or j<0:
            return int(1e9)
        if dp[i][j]!=-1:
            return dp[i][j]
        up=grid[i][j]+self.minPath(i-1,j,grid,dp)
        left=grid[i][j]+self.minPath(i,j-1,grid,dp)
        dp[i][j]=min(up,left)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        return self.minPath(n-1,m-1,grid,dp)
        
