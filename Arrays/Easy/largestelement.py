class Solution:
    def largestElement(self, nums):
        lar=nums[0]
        for i in range(len(nums)):
            if nums[i]>=lar:
                lar=nums[i]
        return lar
