# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

        
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)  
    dp[0] = 0  

    for coin in coins:
        for i in range(coin, amount + 1):  
            dp[i] = min(dp[i], dp[i - coin] + 1)  

    return dp[amount] if dp[amount] != float('inf') else -1  


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount)) 
        
