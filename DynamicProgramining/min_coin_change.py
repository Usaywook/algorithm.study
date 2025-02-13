# find minimum number of coins to make a change for a given amount

def solveRecursive(amount):
    """
    base:
        if n = 0, then 0
        if n < 0, then -1
        f[0] = 0, f[1] = -1, 
    process:
        f[2] = 1, f[3] = 1,  f[4] = 2, f[5] = 1, ...
        f[n] = min(f[n-2], f[n-3], f[n-5]) + 1
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    ans = 1000
    for x in coins:
        k = solveRecursive(amount - x)
        if k == -1:
            continue
        if k < ans:
            ans = k 
            
    return -1 if ans == 1000 else ans + 1

def solveIterative(amount):
    # base
    ans = [-1] * (amount + 1)
    ans[0] = 0
    # process
    for i in range(2, amount+1):
        min = 1000
        for x in coins:
            q = i - x
            if q < 0:
                continue
            k = ans[q] 
            if k == -1:
                continue
            if k < min:
                min = k
        ans[i] = -1 if min == 1000 else min + 1
            
    return ans[amount]
    
if __name__ == '__main__':    
    global coins
    coins = [2, 3, 5]
    amount = 11
    ans = solveRecursive(amount)
    print(ans)
    ans = solveIterative(amount)
    print(ans)