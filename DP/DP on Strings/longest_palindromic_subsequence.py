# Tabulation

class Solution:
    """ Function to calculate the length of 
    the Longest Palindromic Subsequence """
    def func(self, s1, s2):
        n = len(s1)
        m = len(s2)

        # Declare a 2D DP array to store length of the LCS
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Initialize first row and first column to 0
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(m + 1):
            dp[0][i] = 0

        # Fill in the DP array
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        
        # The value at dp[n][m] contains length of the LCS
        return dp[n][m]

    """ Function to calculate the length of 
    the Longest Palindromic Subsequence """
    def longestPalinSubseq(self, s):
        # Store a reversed copy of the string
        t = s[::-1]

        """ Call the LCS function to find the 
        length of the Longest Common Subsequence """
        return self.func(s, t)

if __name__ == "__main__":
    s = "bbabcbcab"
    
    # Create an instance of Solution class
    sol = Solution()
    
    # Print the result
    print("The Length of Longest Palindromic Subsequence is", sol.longestPalinSubseq(s))


# Space Optimization
class Solution:
    """ Function to calculate the length of 
    the Longest Palindromic Subsequence"""
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)

        """ Create two arrays to store the 
        previous and current rows of DP values """
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        """ Base Case is covered as we have
        initialized the prev and cur to 0. """

        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]
                else:
                    cur[ind2] = max(prev[ind2], cur[ind2 - 1])
            """ Update the prev array with current values """
            prev = cur[:]
        
        # The value at prev[m] contains length of LCS
        return prev[m]

    def longestPalinSubseq(self, s):
        # Store a reversed copy of the string
        t = s[::-1]

        """ Call the LCS function to find the 
        length of the Longest Common Subsequence"""
        return self.lcs(s, t)

if __name__ == "__main__":
    s = "bbabcbcab"
    
    # Create an instance of Solution class
    sol = Solution()
    
    # Print the result
    print("The Length of Longest Palindromic Subsequence is", sol.longestPalinSubseq(s))
