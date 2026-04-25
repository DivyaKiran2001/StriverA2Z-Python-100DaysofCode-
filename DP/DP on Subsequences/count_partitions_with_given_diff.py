# Memoization
class Solution:
    # Function to count subsets that sum up to target
    def countSubsets(self, nums,d):
        # Initialize dp table with -1 (uncomputed states)
        dp = [[-1] * (target + 1) for _ in range(len(nums))]
        totsum=0
        for i in range(len(nums)):
          totsum+=nums[i]
        if (totsum-d <=0 or (totsum-d)%2):
          return False
        return self.solve(len(nums) - 1, (totsum-d)//2, nums, dp)

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
    # Function to count partitions with given difference
    def countPartitions(self, arr, d):
        # Calculate total sum of array
        totalSum = sum(arr)

        # Check if solution is possible
        if (totalSum + d) % 2 != 0 or d > totalSum:
            return 0

        # Calculate target sum
        K = (totalSum + d) // 2

        # Create dp array of size K+1
        dp = [0] * (K + 1)
        dp[0] = 1

        # If first element <= K, mark it
        if arr[0] <= K:
            dp[arr[0]] += 1

        # Process remaining elements
        for i in range(1, len(arr)):
            curr = [0] * (K + 1)
            curr[0] = 1
            for t in range(K + 1):
                notTake = dp[t]
                take = 0
                if arr[i] <= t:
                    take = dp[t - arr[i]]
                curr[t] = take + notTake
            dp = curr

        return dp[K]


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4]
    d = 1
    print(sol.countPartitions(arr, d))
