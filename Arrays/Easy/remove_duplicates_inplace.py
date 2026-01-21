
#BruteForce
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        # nl=list(s)
        fs=sorted(s)
        i=0
        for x in fs:
            nums[i]=x
            i=i+1
        k=i
        # for i in range(k,len(nums)):
        #     nums[i]='_'

        return k
        # k=len(nl)
        # fl=[]

        # for i in range(len(nums)):
        #     if i<len(nl):
        #         fl.append(nl[i])
        #     else:
        #         s="_"
        #         fl.append(int(s))
        # return k,fl

#Optimal
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
     
        for j in range(1,len(nums)):
            if nums[j] > nums[i]:
                nums[i+1]=nums[j]
                i=i+1
        return i+1 
        
