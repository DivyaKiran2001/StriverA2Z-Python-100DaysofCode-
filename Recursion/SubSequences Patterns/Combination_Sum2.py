class Solution:
     def findCombination(self,ind,target,arr,ans,ds):
        # Base Case
        if target==0:
            ans.append(list(ds))
            return
        # Loop through the elements starting from index 'ind'
        for i in range(ind,len(arr)):
            # Skip duplicates to avoid repeating combinations
            if i>ind and arr[i]==arr[i-1]:
                continue
            
            # If the current element is greater than the remaining target, break the loop
            if arr[i]>target:
                break
            
            # Include the current element in the combination
            ds.append(arr[i])
            
            # Recur with the updated target and next index (i + 1 to avoid repetition)
            self.findCombination(i + 1, target - arr[i], arr, ans, ds)

            # Backtrack by removing the last added element
            ds.pop()
    
    
    def combinationSum2(self, candidates, target):
        #your code goes here
        candidates.sort()
        ans=[]
        ds=[]
        self.findCombination(0,target,candidates,ans,ds)
        return ans
        
