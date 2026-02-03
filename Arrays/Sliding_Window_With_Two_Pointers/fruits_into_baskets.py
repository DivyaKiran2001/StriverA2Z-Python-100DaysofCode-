from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        l=0
        r=0
        maxlen=0
        basket=defaultdict(int)
        while r<n:
            basket[fruits[r]]+=1
            if len(basket)>2:
                while len(basket)>2:
                    basket[fruits[l]] -= 1
                    if basket[fruits[l]]==0:
                        del basket[fruits[l]]
                    l+=1
            if len(basket)<=2:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen


        
