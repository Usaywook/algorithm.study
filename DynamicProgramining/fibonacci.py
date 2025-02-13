# base : f[n] = n if 0 or 1
# recursive case : f[n] = f[n-1] + f[n-2]

def FiboRecursive(n):
    # base case
    if n < 2:
        return n
    
    # top-down
    return FiboRecursive(n-1) + FiboRecursive(n-2)

def FiboIteratuve(n):
    if n < 2:
        return n
    memo = [0] * (n + 1)
    # base case
    memo[1] = 1
    
    # bottom-up
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

def solve(n):
    """
    Application of Fibonacci  
    base case :
        f[0] = 0
        f[1] = 1
        f[2] = 2    
    iterative case :    
        f[n] = f[n-1] + f[n-2]
    how many ways to climb to the top with jump 1 or 2 steps
    """
    array = [0] * (n + 1)
    array[1] = 1
    array[2] = 2
    for i in range(3, n + 1):
        array[i] = array[i-1] + array[i-2]
    return array[n]

if __name__ == '__main__':
    print(FiboRecursive(10))
    print(FiboIteratuve(10))
    print(solve(10))