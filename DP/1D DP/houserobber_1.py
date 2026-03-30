class Solution:
    def solve(self,arr,i,dp):
        if i<0:
            return 0
        if i==0:
            return arr[0]
        if dp[i]!=-1:
            return dp[i]
        # Pick the element
        pick=arr[i]+self.solve(arr,i-2,dp)
        notpick=0+self.solve(arr,i-1,dp)
        dp[i]=max(pick,notpick)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.solve(nums,n-1,dp)

        
