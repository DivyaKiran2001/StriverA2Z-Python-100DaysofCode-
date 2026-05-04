# Tabulation

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)

        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        len_lcs=dp[n][m]

        # Return total operations = deletions + insertions
        # no_of_deletions=n-len(lcs)
        # no_of_insertions=m-len(lcs)

        #return (n-len_lcs)+(m-len_lcs)
        return n+m-2*(len_lcs)


# Space Optimization

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)

        prev=[0]*(m+1)
        curr=[0]*(m+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    val=1+prev[j-1]
                    curr[j]=val
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev[:]=curr[:]
        
        len_lcs=prev[m]
        return (n-len_lcs)+(m-len_lcs)
        
