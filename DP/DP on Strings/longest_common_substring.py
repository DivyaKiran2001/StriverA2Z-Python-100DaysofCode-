# Tabulation

class Solution:
    def longestCommonSubstr(self, str1, str2):
        n=len(str1)
        m=len(str2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        ans=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                # Characters match, increment substring length
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]

                    ans=max(ans,dp[i][j])

                else:
                    dp[i][j]=0
        return ans


# Space Optimization Approach

class Solution:
    def longestCommonSubstr(self, str1, str2):
        n=len(str1)
        m=len(str2)
        
        """ Initialize two lists to store 
        previous and current row values """

        prev=[0]*(m+1)
        cur=[0]*(m+1)

        ans=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    val=1+prev[j-1]
                    cur[j]=val

                    ans=max(ans,val)
                else:
                    cur[j]=0
            prev[:]=cur[:]
        return ans
    
