class Solution:
    def findSums(self,ind,csum,nums,sums):
        if ind==len(nums):
            sums.append(csum)
            return
        # Include current element
        self.findSums(ind+1,csum+nums[ind],nums,sums)
        # Exclude current element
        self.findSums(ind+1,csum,nums,sums)


    def subsetSums(self, nums):
        #your code goes here
        sums=[]
        self.findSums(0,0,nums,sums)
        sums.sort()
        return sums
