from math import gcd

def greedy_coins(values: list[int], target: int) -> list[int]:
    values.sort(reverse=True)
    coins = []
    for value in values:
        while(value <= target):
            coins.append(value)
            target -= value
    
    return coins


def power_coins(base: int, k: int, target: int) -> list[int]:
    values = [base**i for i in range(k + 1)]
    values.sort(reverse=True)
    coins = []
    for value in values:
        while (value <= target):
            coins.append(value)
            target -= value

    return coins
            
def coins_dp(coins: list[int], target: int, dp = []) -> int:
    if(dp == []):
        dp = [-1 for _ in range(target+1)]
        dp[0] = 0

    if(dp[target] != -1): return dp[target]

    dp[target] = 1 + min([coins_dp(coins, target - coin, dp) for coin in coins if target - coin >= 0])
    return dp[target]
    
coins = [25, 10, 5, 4, 1]
total = 108
print("Power: ", power_coins(5, 3, total))
print("Greedy: ", greedy_coins(coins, total))
print("DP: ", coins_dp(coins, total))

        






    

    
