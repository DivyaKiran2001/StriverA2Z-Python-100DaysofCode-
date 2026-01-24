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
        
# Using Two pointer approach
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1   # move window start
            else:
                max_len = max(max_len, right - left + 1)

        return max_len
