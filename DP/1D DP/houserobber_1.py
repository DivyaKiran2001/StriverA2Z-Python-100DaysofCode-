# Memoization
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

# Tabulation

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            notpick=0+dp[i-1]
            dp[i]=max(pick,notpick)
        return dp[n-1]
# Space Optimization
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2=0
        prev=nums[0]
        for i in range(1,len(nums)):
            pick=nums[i]+prev2
            notpick=prev
            curr=max(pick,notpick)
            prev2=prev
            prev=curr
        return prev
        
        
