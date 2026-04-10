# Memoization
class Solution:
    def countPaths(self, i, j, dp):
        # Base Case
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        
        # Check memoization
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Recursive calls
        up = self.countPaths(i - 1, j, dp)
        left = self.countPaths(i, j - 1, dp)
        
        dp[i][j] = up + left
        return dp[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.countPaths(m - 1, n - 1, dp)


# ---- Function Calling ----
if __name__ == "__main__":
    m = 3
    n = 3
    
    obj = Solution()
    result = obj.uniquePaths(m, n)
    
    print("Number of Unique Paths:", result)


# Tabulation
class Solution:
    def countPaths(self,m,n,dp):
        for i in range(m):
            for j in range(n):
                # Base Condition
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up=0
                left=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[m-1][n-1]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return self.countPaths(m,n,dp)
        
  
