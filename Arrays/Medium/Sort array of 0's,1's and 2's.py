#Sort Colors (Sort 0's,1's and 2's) using Dutch National Flag Algorithm  i.e using three pointers


#brute and better 
Take a dictionary andstore the frequency of 0's ,1's and 2's and replace in the array

#Optimal Solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low=low+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            elif nums[mid]==2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high=high-1
        
    
