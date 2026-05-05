# Tabulation

# Class to compute shortest common supersequence
class Solution:

    # Function to return shortest common supersequence of two strings
    def shortestSupersequence(self, s1: str, s2: str) -> str:

        # Get the lengths of the strings
        n = len(s1)
        m = len(s2)

        # Create a 2D DP table to store LCS lengths
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table using bottom-up approach
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # If characters match, take diagonal + 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                # Otherwise, take max from top or left
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Start from bottom-right and build the supersequence
        i, j = n, m
        result = []

        # Traverse in reverse to collect characters
        while i > 0 and j > 0:

            # If characters are equal, include once and move diagonally
            if s1[i - 1] == s2[j - 1]:
                result.append(s1[i - 1])
                i -= 1
                j -= 1

            # Move in direction of greater value
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(s1[i - 1])
                i -= 1
            else:
                result.append(s2[j - 1])
                j -= 1

        # Add remaining characters from s1
        while i > 0:
            result.append(s1[i - 1])
            i -= 1

        # Add remaining characters from s2
        while j > 0:
            result.append(s2[j - 1])
            j -= 1

        # Reverse the result as it was built in reverse
        result.reverse()

        # Join the list to form final string
        return ''.join(result)

# Driver code
if __name__ == "__main__":

    # Define input strings
    s1 = "brute"
    s2 = "groot"

    # Create object of Solution class
    obj = Solution()

    # Call the function and print the result
    print("The Shortest Common Supersequence is", obj.shortestSupersequence(s1, s2))
