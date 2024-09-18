def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with infinity (impossible cases)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make a total of 0

    # Iterate over each coin and fill dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1

# Testing with example cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
