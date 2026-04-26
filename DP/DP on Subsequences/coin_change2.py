# Memoization

class Solution:
    def countWaysToMakeChangeUtil(self, arr, ind, T, dp):
        if ind == 0:
            return 1 if T % arr[0] == 0 else 0
        if dp[ind][T] != -1:
            return dp[ind][T]

        notTaken = self.countWaysToMakeChangeUtil(arr, ind - 1, T, dp)
        taken = 0
        if arr[ind] <= T:
            taken = self.countWaysToMakeChangeUtil(arr, ind, T - arr[ind], dp)

        dp[ind][T] = notTaken + taken
        return dp[ind][T]

    def countWaysToMakeChange(self, arr, n, T):
        dp = [[-1 for _ in range(T + 1)] for _ in range(n)]
        return self.countWaysToMakeChangeUtil(arr, n - 1, T, dp)

if __name__ == "__main__":
    arr = [1, 2, 3]
    target = 4
    n = len(arr)

    sol = Solution()
    print("The total number of ways is", sol.countWaysToMakeChange(arr, n, target))

# Tabulation

def countWaysToMakeChange(arr, n, T):
    # Create a DP table to store the number of ways for different target amounts
    dp = [[0 for j in range(T + 1)] for i in range(n)]
    
    # Initialize the base condition for the first element in the array
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = 1
        # Else condition is automatically fulfilled, as dp array is initialized to zero

    # Iterate through the array elements and target amounts
    for ind in range(1, n):
        for target in range(T + 1):
            # Calculate the number of ways when the current element is not taken
            notTaken = dp[ind - 1][target]

            # Initialize a variable for the number of ways when the current element is taken
            taken = 0
            if arr[ind] <= target:
                taken = dp[ind][target - arr[ind]]

            # Store the total number of ways in the DP table
            dp[ind][target] = notTaken + taken

    # Return the total number of ways for the given target amount
    return dp[n - 1][T]

def main():
    arr = [1, 2, 3]
    target = 4
    n = len(arr)
    print("The total number of ways is", countWaysToMakeChange(arr, n, target))

if __name__ == "__main__":
    main()
