# Memoization

class Solution:
    def solve(self,i,j,triangle,n,dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        
        # Base Case
        if i==n-1:
            return triangle[i][j]
        
        down=triangle[i][j]+self.solve(i+1,j,triangle,n,dp)
        diagonal=triangle[i][j]+self.solve(i+1,j+1,triangle,n,dp)

        dp[i][j]=min(down,diagonal)
        return dp[i][j]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        return self.solve(0,0,triangle,n,dp)



# Tabulation


# Steps

#1 Start by creating a 2D table with the same dimensions as the triangle to store intermediate results.
#2 Fill the last row of this table with the same values from the last row of the triangle since that's the base of the problem.
#3 Begin filling the table from the second-last row and move upwards until you reach the top row.
#4 For each cell, compute the minimum of the two possible paths, directly downward and diagonally downward and add the current triangle value.
#5 Since the table is being filled bottom-up, by the time you reach any cell, the needed values from the row below are already available.
#6 After filling the entire table, the topmost cell will hold the minimum path sum from top to bottom of the triangle.

class Solution:
    def solve(self,i,j,triangle,n,dp):
        # Fill last row

        for j in range(n):
            dp[n-1][j]=triangle[n-1][j]
        
        # Fill rest of dp from bottom to top
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                down = triangle[i][j]+dp[i+1][j]
                diagonal = triangle[i][j]+dp[i+1][j+1]
                dp[i][j]=min(down,diagonal)
            
        return dp[0][0]


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        return self.solve(0,0,triangle,n,dp)
        
