class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        ma=n/2
        for i in range(len(nums)):
            if nums[i] in d:
                x=nums[i]
                d[x]+=1
            else:
                x=nums[i]
                d[x]=1
        print(d)
        for i in d:
            if d[i]>ma:
                return i
        
