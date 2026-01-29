# Brute force solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                        st.add(triplet)
        return [list(triplet) for triplet in st]        


# Better solution using hashmap

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        n=len(nums)
        for i in range(n):
            hashset=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in hashset:
                    triplet=tuple(sorted([nums[i],nums[j],third]))
                    ans.add(triplet)
                hashset.add(nums[j])
        return [list(triplet) for triplet in ans]


# Optimal Solution using Two pointer Approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum<0:
                    j+=1
                elif sum>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
        return ans

