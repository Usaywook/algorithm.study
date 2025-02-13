
def solve1(amount, coins):   
    cache={}
    def dp(n,m):
        """
        Args:
            n (int): The index for coins
            m (int): The sum of coins to make with coins

        Returns:
            int: The number of cases to make m with n coins.
        """    
        if (n,m) in cache:
            return cache[(n,m)]
        if m == 0 and n == 0:
            return 1
        elif m < 0 or n == 0:
            return 0
        
        ans = dp(n, m - coins[n-1])
        ans += dp(n-1, m)
        cache[(n,m)] = ans
        return ans
    return dp(len(coins), amount)

def solve2(amount, coins):
    N = len(coins)
    M = amount    
    memo = [[1]*(M+1) for _ in range(N+1)]
    memo[0][1:] = [0]*M
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            k = j - coins[i-1]
            memo[i][j] = memo[i-1][j]
            if k < 0:
                continue
            memo[i][j] += memo[i][k]
        
    return memo[-1][-1]

coins = [1,2,3]
amount = 5

# print(solve1(amount, coins))
print(solve2(amount, coins))