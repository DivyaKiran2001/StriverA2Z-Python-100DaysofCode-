class Solution:

    # To Check if the cell is within maze and valid to move
    def isSafe(self,x,y,n,maze,visited):
        return (0<=x<n and 0<=y<n and 
        maze[x][y]==1 and visited[x][y]==0)

    def solve(self, x, y, n, maze, visited, path, res):
        # Base Case
        if x==n-1 and y==n-1:
            res.append(path)
            return
        
        ## Mark the cell as visited
        visited[x][y]=1

        # Try moving down
        if self.isSafe(x+1,y,n,maze,visited):
            self.solve(x+1,y,n,maze,visited,path+"D",res)
        
        #Try moving left
        if self.isSafe(x,y-1,n,maze,visited):
            self.solve(x,y-1,n,maze,visited,path+"L",res)
        
        #Try moving Right
        if self.isSafe(x,y+1,n,maze,visited):
            self.solve(x,y+1,n,maze,visited,path+"R",res)
        
        #Try moving Up
        if self.isSafe(x-1,y,n,maze,visited):
            self.solve(x-1,y,n,maze,visited,path+"U",res)

        # Backtrack: unmark cell as visited
        visited[x][y] = 0

    def findPath(self, grid):
        #your code goes here
        n = len(grid)
        res=[]
        vis=[[0]*n for _ in range(n)]
        if grid[0][0]==1:
            self.solve(0,0,n,grid,vis,"",res)
        return res
