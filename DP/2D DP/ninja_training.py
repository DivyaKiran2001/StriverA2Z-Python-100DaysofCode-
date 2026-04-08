# Memoization

class Solution:
    def maxpoints(self, day, last, points, dp):
        if dp[day][last]!=-1:
            return dp[day][last]
         # Base case: day 0
        if day == 0:
            maxi=0
            for i in range(3):
                if i!=last:
                    maxi=max(maxi,points[0][i])
            dp[day][last]=maxi
            return maxi
        maxi=0
        for i in range(3):
            if i!=last:
                activity=points[day][i]+self.maxpoints(day-1,i,points,dp)
                maxi = max(maxi, activity)

        dp[day][last] = maxi
        return maxi



    def ninjaTraining(self, matrix):
        n=len(matrix)
        dp=[[-1]*4 for _ in range(n)]
        return self.maxpoints(n-1,3,matrix,dp)
