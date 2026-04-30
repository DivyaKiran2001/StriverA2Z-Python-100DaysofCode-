# Tabulation

class Solution:

    # Function to calculate LCS
    def lcs(self, s1, s2):

        # Get sizes
        n = len(s1)
        m = len(s2)

        # Create dp array
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill dp array
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):

                # If characters match
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

                # If not
                else:
                    dp[ind1][ind2] = max(
                        dp[ind1 - 1][ind2], 
                        dp[ind1][ind2 - 1]
                    )

        # Return result
        return dp[n][m]

    # Function to calculate LPS
    def longestPalindromeSubsequence(self, s):
        
        # Reverse string
        t = s[::-1]

        # Return LCS of s and reverse
        return self.lcs(s, t)

    # Function to get min insertions
    def minInsertion(self, s):

        # Get LPS
        k = self.longestPalindromeSubsequence(s)

        # Return result
        return len(s) - k


# Main driver
if __name__ == "__main__":
    
    # Create object
    sol = Solution()

    # Input string
    s = "abcaa"

    # Print result
    print("The Minimum insertions required to make string palindrome:",
          sol.minInsertion(s))


# Space Optimization

class Solution:

    # Function to compute LCS with space optimization
    def lcs(self, s1, s2):
        n, m = len(s1), len(s2)
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):

                # If characters match
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]

                # Else take max
                else:
                    cur[ind2] = max(prev[ind2], cur[ind2 - 1])

            # Move cur to prev
            prev = cur[:]

        return prev[m]

    # Function to compute LPS
    def longestPalindromeSubsequence(self, s):
        t = s[::-1]
        return self.lcs(s, t)

    # Function to compute min insertions
    def minInsertion(self, s):
        n = len(s)
        k = self.longestPalindromeSubsequence(s)
        return n - k

# Driver code
if __name__ == "__main__":
    sol = Solution()
    s = "abcaa"
    print("The Minimum insertions required to make string palindrome:",
          sol.minInsertion(s))

