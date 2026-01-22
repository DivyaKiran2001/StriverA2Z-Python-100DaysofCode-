class Solution:
   def rotate(self, nums: List[int], k: int) -> None:
       """
       Do not return anything, modify nums in-place instead.
       """
       fele=nums[0]
       for i in range(1,len(nums)):
           nums[i-1]=nums[i]
       nums[-1]=fele
       return nums
