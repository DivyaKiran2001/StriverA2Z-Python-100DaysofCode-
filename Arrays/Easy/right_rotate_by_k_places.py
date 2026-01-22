	# Rotate Array by right by k places
	class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # 1. Normalize k (crucial for cases like k=7, n=2)
        k = k % n 
        
        if k == 0: return

        # 2. Store the first n-k elements
        temp = []
        for i in range(n - k):
            temp.append(nums[i])
            
        # 3. Move the last k elements to the front
        # Your original loop: for i in range(k)
        # This correctly fills the first k slots of nums
        for i in range(k):
            nums[i] = nums[n - k + i]
    
        # 4. Put the temp elements back into the end of nums
        j = 0
        for i in range(k, n):
            nums[i] = temp[j]
            j += 1
			
