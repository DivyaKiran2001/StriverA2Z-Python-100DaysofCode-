class Solution:
    def frogJump(self, heights, k):
        n=len(heights)
        dp=[-1]*n
        dp[0]=0
        for i in range(1,n):
            mmSteps = float('inf')
            for j in range(1,k+1):
                if i-j>=0:
                    jump=dp[i-j]+abs(heights[i]-heights[i-j])
                    mmSteps=min(mmSteps,jump)
            dp[i]=mmSteps
        return dp[n-1]
