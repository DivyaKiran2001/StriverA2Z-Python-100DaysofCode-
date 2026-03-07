class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(ind,target,ds):
            if ind==len(candidates):
                if target==0:
                    res.append(ds[:])
                return
            # Pick Case
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                backtrack(ind,target-candidates[ind],ds)
                ds.pop()
            # Not Pick Case
            backtrack(ind+1,target,ds)
        backtrack(0,target,[]) 
        return res           
        
        
