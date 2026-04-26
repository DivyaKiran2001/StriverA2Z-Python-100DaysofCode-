# Tabulation

class Solution:
    def findcommonlcs(self, i, j, s1, s2, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.findcommonlcs(i - 1, j - 1, s1, s2, dp)
        else:
            dp[i][j] = max(
                self.findcommonlcs(i - 1, j, s1, s2, dp),
                self.findcommonlcs(i, j - 1, s1, s2, dp)
            )

        return dp[i][j]

    def lcs(self, str1, str2):
        n = len(str1)
        m = len(str2)

        dp = [[-1] * m for _ in range(n)]

        return self.findcommonlcs(n - 1, m - 1, str1, str2, dp)
