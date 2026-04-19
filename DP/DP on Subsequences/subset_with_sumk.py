# Memoization


class Solution:
    def subSetSumUtil(self, ind, target, arr, dp):
        if target==0:
            return True
        # Base case: first index check
        if ind==0:
            return arr[0]==target
        
         # If already computed
        if dp[ind][target] != -1:
            return dp[ind][target] == 1

        # Choice 1: not take the element
        nottake=self.subSetSumUtil(ind-1,target,arr,dp)

        # Choice 2: take the element if possible
        take=False
        if arr[ind]<=target:
            take=self.subSetSumUtil(ind-1,target-arr[ind],arr,dp)
        
        # Store result
        dp[ind][target] = 1 if (notTaken or taken) else 0
        return notTaken or taken

    def isSubsetSum(self, arr, target):
        n=len(arr)
        dp=[[-1]*(k+1) for _ in range(n)]
        return self.subSetSumUtil(n-1,target,arr,dp)


# Tabulation

class Solution:
    def subsetSumToK(self, n, k, arr):
        # Initialize DP table with False values
        dp = [[False] * (k + 1) for _ in range(n)]

        # Base case: sum 0 can always be formed with empty subset
        for i in range(n):
            dp[i][0] = True

        # Base case: if first element <= k, set that position True
        if arr[0] <= k:
            dp[0][arr[0]] = True

        # Fill the DP table iteratively
        for ind in range(1, n):
            for target in range(1, k + 1):
                # Option 1: not take current element
                not_taken = dp[ind - 1][target]

                # Option 2: take current element if possible
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]

                # Current cell is True if either option is True
                dp[ind][target] = not_taken or taken

        # Final answer: can sum k be formed using all elements?
        return dp[n - 1][k]


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)
    sol = Solution()

    if sol.subsetSumToK(n, k, ar



