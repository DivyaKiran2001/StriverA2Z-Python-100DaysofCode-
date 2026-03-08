class Solution:
    def backtrack(self,start,nums,ds,res):
        res.append(list(ds))

        for i in range(start,len(nums)):
            # Skip duplicates
            if i>start and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            self.backtrack(i+1,nums,ds,res)
            ds.pop()

    def subsetsWithDup(self, nums):
        #your code goes here
        nums.sort()
        res=[]
        self.backtrack(0,nums,[],res)
        return res
