class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints[:k])
        maxsum=total
        # Slide the window: remove from front, add from back
        for i in range(k):
            # Subtract from the front
            total-=cardPoints[k-1-i]
            # Add from the back
            total+=cardPoints[n-1-i]
            maxsum=max(maxsum,total)
        return maxsum
        
