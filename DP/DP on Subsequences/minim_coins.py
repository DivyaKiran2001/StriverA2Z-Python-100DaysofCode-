# Memoization
from typing import List

class Solution:
    def countcoins(self, ind, coins, amount, dp):
        # Base case: only first coin is available
        if ind == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return float('inf')

        # Check if already computed
        if dp[ind][amount] != -1:
            return dp[ind][amount]

        # Option 1: Do not take current coin
        nottake = self.countcoins(ind - 1, coins, amount, dp)

        # Option 2: Take current coin (if possible)
        take = float('inf')
        if coins[ind] <= amount:
            take = 1 + self.countcoins(ind, coins, amount - coins[ind], dp)

        # Store result
        dp[ind][amount] = min(take, nottake)
        return dp[ind][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # DP table initialization
        dp = [[-1] * (amount + 1) for _ in range(n)]

        ans = self.countcoins(n - 1, coins, amount, dp)

        # If not possible to make amount
        if ans == float('inf'):
            return -1

        return ans

# Tabulation

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # DP table
        dp = [[0] * (amount + 1) for _ in range(n)]

        # Base case: using only first coin
        for T in range(amount + 1):
            if T % coins[0] == 0:
                dp[0][T] = T // coins[0]
            else:
                dp[0][T] = float('inf')

        # Fill the DP table
        for ind in range(1, n):
            for T in range(amount + 1):

                # Not take current coin
                nottake = dp[ind - 1][T]

                # Take current coin
                take = float('inf')
                if coins[ind] <= T:
                    take = 1 + dp[ind][T - coins[ind]]

                dp[ind][T] = min(take, nottake)

        ans = dp[n - 1][amount]

        # If not possible to make the amount
        if ans == float('inf'):
            return -1

        return ans
