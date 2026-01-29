#Maximum Subarray Sum (Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tsum=0
        maxi=float('-inf')
        for i in range(len(nums)):
            tsum+=nums[i]
            if tsum>maxi:
                maxi=tsum
            if tsum<0:
                tsum=0
        return maxi


# Print subarray with maximum subarray sum (extended version of above problem)

class Solution:
    def maxSubArray(self, nums):
        maxi=float('-inf')
        tsum=0
        start=0
        anstart=0
        ansend=0
        for i in range(len(nums)):
            if tsum==0:
                start=i
            tsum+=nums[i]
            if tsum>maxi:
                maxi=tsum
                anstart=start
                ansend=i
         
            if tsum<0:
                tsum=0
        print(nums[anstart:ansend+1])
        return maxi
        
