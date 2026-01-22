#brute
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(k):
            temp.append(nums[i])
        for i in range(k,len(nums)):
            nums[i-k]=nums[i]
        j=0
        l=len(nums)-k
        for i in range(l,len(nums)):
            nums[i]=temp[j]
            j=j+1
        return nums


			
	class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        for i in range(k):
            temp.append(nums[i])
        for i in range(k,len(nums)):
            nums[i-k]=nums[i]
    
        l=len(nums)-k
        for i in range(l,len(nums)):
            nums[i]=temp[i-(l-k)]
        
        return nums
				
				
      
#better	
reverse(a,a+k)
reverse(a+k,a+len(nums))
reverse(a,a+len(nums))
