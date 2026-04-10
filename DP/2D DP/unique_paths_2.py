class Solution:
    def countPaths(self, i, j,grid, dp):
        # Base Case
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0 or grid[i][j]==1:
            return 0
        
        # Check memoization
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Recursive calls
        up = self.countPaths(i - 1, j,grid, dp)
        left = self.countPaths(i, j - 1,grid, dp)
        
        dp[i][j] = up + left
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.countPaths(m - 1, n - 1,obstacleGrid,dp)
        
