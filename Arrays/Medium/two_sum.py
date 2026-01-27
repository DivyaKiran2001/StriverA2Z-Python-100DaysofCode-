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
        
# Optimal - Using Two pointer Approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices=[(num,idx) for idx,num in enumerate(nums)]
        nums_with_indices.sort(key=lambda x:x[0])
        left=0
        right=len(nums)-1
        while left<right:
            current_sum=nums_with_indices[left][0]+nums_with_indices[right][0]
            if current_sum==target:
                return [nums_with_indices[left][1], nums_with_indices[right][1]]
            elif current_sum<target:
                left+=1
            else:
                right-=1
        return [-1,-1]



