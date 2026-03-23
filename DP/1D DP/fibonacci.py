# Memoization

def fib_memo(n, dp):
    # Base case
    if n <= 1:
        return n
    
    # If already computed, return it
    if dp[n] != -1:
        return dp[n]
    
    # Store result in dp array
    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)
    
    return dp[n]


# Driver code
n = 10
dp = [-1] * (n + 1)
print(fib_memo(n, dp))

# Tabulation

def fib_tab(n):
    # Edge case
    if n <= 1:
        return n
    
    # DP array
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = 1
    
    # Fill dp array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# Driver code
n = 10
print(fib_tab(n))

