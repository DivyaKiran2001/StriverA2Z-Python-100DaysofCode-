#brute

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0,len(nums)+1):
            if i in nums:
                pass
            else:
                return i


#optimal 1 using sum formula

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1 = int((n*(n+1))/2)
        sum2 = 0
        for i in range(len(nums)):
            sum2+=nums[i]
        return sum1-sum2

#optimal 2 using XOR approach 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1=0
        xor2=0
        for i in range(1,len(nums)+1):
            xor1^=i
        for n in nums:
            xor2^=n
        return xor1^xor2
