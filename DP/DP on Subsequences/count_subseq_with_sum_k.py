# Memoization
class Solution:
    # Function to count subsets that sum up to target
    def countSubsets(self, nums, target):
        # Initialize dp table with -1 (uncomputed states)
        dp = [[-1] * (target + 1) for _ in range(len(nums))]
        return self.solve(len(nums) - 1, target, nums, dp)

    # Recursive helper with memoization
    def solve(self, index, target, nums, dp):
        # Base case: if target is 0, we found a valid subset
        if target == 0:
            return 1

        # Base case: if we are at index 0, check if nums[0] equals target
        if index == 0:
            return 1 if nums[0] == target else 0

        # If already computed, return from dp
        if dp[index][target] != -1:
            return dp[index][target]

        # Case 1: Exclude current element
        notTake = self.solve(index - 1, target, nums, dp)

        # Case 2: Include current element (if it is not greater than target)
        take = 0
        if nums[index] <= target:
            take = self.solve(index - 1, target - nums[index], nums, dp)

        # Store result in dp and return
        dp[index][target] = take + notTake
        return dp[index][target]

# Tabulation

class Solution:
    def countSubsets(self, arr, K):
        # Get number of elements
        n = len(arr)

        # Create dp table with dimensions n x (K+1)
        dp = [[0] * (K + 1) for _ in range(n)]

        # Base case: one subset (empty set) makes sum 0
        dp[0][0] = 1

        # If first element is <= K, mark dp[0][arr[0]] as 1
        if arr[0] <= K:
            dp[0][arr[0]] = 1

        # Fill the table
        for i in range(1, n):
            for target in range(K + 1):
                # Exclude current element
                notTake = dp[i - 1][target]

                # Include current element if possible
                take = 0
                if arr[i] <= target:
                    take = dp[i - 1][target - arr[i]]

                # Total ways
                dp[i][target] = notTake + take

        # Final answer
        return dp[n - 1][K]


# Driver code
arr = [1, 2, 3, 3]
K = 6
obj = Solution()
print(obj.countSubsets(arr, K))


