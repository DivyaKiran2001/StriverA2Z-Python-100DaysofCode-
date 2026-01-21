#Brute force
class Solution:
    def secondLargestElement(self, nums):
        li=nums.sort()
        lar=li[n-1]
        slar=0
        for i in range(len(li)-2,0,-1):
            if li[i] != lar :
                slar=li[i]
                break
        return slar

#Better
class Solution:
    def secondLargestElement(self, nums):
      lar=nums[0]
      slar=-1
      for i in range(len(nums)):
        if nums[i]>lar:
          lar=nums[i]
      for i in range(len(nums)):
        if nums[i]>slar and nums[i]!=lar:
          slar=nums[i]
      return slar

#Optimal
class Solution:
    def secondLargestElement(self, nums):
        lar=nums[0]
        slar=-1
        for i in range(1,len(nums)):
            if nums[i]>lar:
                slar=lar
                lar=nums[i]
            elif nums[i]<lar and nums[i]>slar:
                slar=nums[i]
        return slar

class Solution:
    def secondSmallestElement(self, nums):
        small=nums[0]
        ssmall=-1
        for i in range(1,len(nums)):
            if nums[i]<small:
                ssmall=small
                small=nums[i]
            elif nums[i]!=small and nums[i]<ssmall:
                ssmall=nums[i]
        return ssmall


        
    
