class Solution:
    def isarraySorted(self, nums):
      for i in range(1,len(nums)):
        if nums[i]>=nums[i-1]:
          pass
        else:
          return false
      return true
