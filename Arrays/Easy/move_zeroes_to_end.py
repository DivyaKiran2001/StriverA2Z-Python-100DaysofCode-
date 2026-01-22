#brute
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        for i in range(len(nums)):
            print(nums[i])
            if nums[i]!=0:
                print("hi")
                temp.append(nums[i])
        print(temp)
        j=0
        for i in range(len(nums)):
            if i< len(temp):
                nums[i]=temp[j]
                j+=1
            elif i>=len(temp):
                nums[i]=0
        return nums

#optimal

        
