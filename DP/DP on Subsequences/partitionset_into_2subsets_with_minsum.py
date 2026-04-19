# Memoization

class Solution:
    # Helper method for subset sum with memoization
    def subsetSumUtil(self, ind, target, arr, dp):
        # Base case: If target is zero, subset is always possible
        if target == 0:
            dp[ind][target] = True
            return True

        # Base case: If only first element is considered, check if equals target
        if ind == 0:
            dp[ind][target] = (arr[0] == target)
            return dp[ind][target]

        # Return cached result if already computed
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Recursive case: Exclude current element
        notTaken = self.subsetSumUtil(ind - 1, target, arr, dp)

        # Recursive case: Include current element if it fits target
        taken = False
        if arr[ind] <= target:
            taken = self.subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

        # Store result and return
        dp[ind][target] = notTaken or taken
        return dp[ind][target]

    # Function to find minimum absolute difference between two subsets
    def minSubsetSumDifference(self, arr, n):
        # Calculate total sum of elements
        totSum = sum(arr)

        # Initialize dp array with -1 for uncomputed states
        dp = [[-1 for _ in range(totSum + 1)] for _ in range(n)]

        # Compute subset sums for all targets from 0 to total sum
        for i in range(totSum + 1):
            self.subsetSumUtil(n - 1, i, arr, dp)

        # Initialize minimum difference to large number
        mini = float('inf')

        # Check all achievable subset sums in last dp row
        for s1 in range(totSum + 1):
            if dp[n - 1][s1]:
                # Calculate complementary subset sum and difference
                s2 = totSum - s1
                diff = abs(s1 - s2)

                # Update minimum difference
                mini = min(mini, diff)

        return mini

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)

    solver = Solution()

    print("The minimum absolute difference is:", solver.minSubsetSumDifference(arr, n))


# Tabulation

class Solution:
    # Function to find the minimum absolute difference between two subset sums
    def minSubsetSumDifference(self, arr, n):
        totSum = 0

        # Calculate the total sum of the array
        for i in range(n):
            totSum += arr[i]

        # Initialize a DP table to store the results of the subset sum problem
        dp = [[False] * (totSum + 1) for _ in range(n)]

        # Base case: If no elements are selected (sum is 0), it's a valid subset
        for i in range(n):
            dp[i][0] = True

        # Initialize the first row based on the first element of the array
        if arr[0] <= totSum:
            dp[0][arr[0]] = True

        # Fill in the DP table using a bottom-up approach
        for ind in range(1, n):
            for target in range(1, totSum + 1):
                # Exclude the current element
                notTaken = dp[ind - 1][target]

                # Include the current element if it doesn't exceed the target
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]

                dp[ind][target] = notTaken or taken

        mini = int(1e9)
        for i in range(totSum + 1):
            if dp[n - 1][i]:
                # Calculate the absolute difference between two subset sums
                diff = abs(i - (totSum - i))
                mini = min(mini, diff)

        return mini

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)

    sol = Solution()
    print("The minimum absolute difference is:", sol.minSubsetSumDifference(arr, n))
