# Memoization (Top Down Approach)

class Solution:
    def solve(self,ind,a,dp):
        if ind==0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        left=self.solve(ind-1,a,dp)+abs(a[ind]-a[ind-1])
        right=float('inf')
        if ind>1:
            right=self.solve(ind-2,a,dp)+abs(a[ind]-a[ind-2])
        dp[ind]=min(left,right)
        return dp[ind]
    def frogJump(self, heights):
        if not heights:
            return 0
        n=len(heights)
        dp=[-1]*n
        return self.solve(n-1,heights,dp)


# Tabulation

class Solution:  
    def frogJump(self, heights):
        if not heights:
            return 0
        n=len(heights)
        dp=[-1]*n
        dp[0]=0
        for ind in range(1,n):
            left=dp[ind-1]+abs(heights[ind]-heights[ind-1])
            right=float('inf')
            if ind>1:
                right=dp[ind-2]+abs(heights[ind]-heights[ind-2])
            dp[ind]=min(left,right)
        return dp[n-1]

