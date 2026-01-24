class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxl=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
                maxl=max(maxl,cnt)
            else:
                cnt=0
        return maxl
        
