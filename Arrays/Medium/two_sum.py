# brute

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                res=nums[i]+nums[j]
                if res==target:
                    l.extend([i,j])

        return l


# Better - Using HashMap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in hm:
                return [hm[rem],i]
            hm[nums[i]]=i
        return [-1,-1]

