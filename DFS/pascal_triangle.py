def pascalTriangleRecursive(row, col):
    # base case
    if col == 0 or col == row:
        return 1
    
    # recursive case
    return pascalTriangleRecursive(row-1, col-1) + pascalTriangleRecursive(row-1, col)

def pascalTriangleTopDown(row, col):
    stack = [(row, col)]
    ans = 0
    while stack:
        r, c  = stack.pop()
        # base case
        if c == 0 or c == r:
            ans += 1
            continue
        
        # save the stack
        stack.extend([(r-1, c), (r-1, c-1)])
        
    return ans

def pascalTriangleBottomUp(n, k):
    # Start with the base case
    ans = [[1]*(i+1) for i in range(n+1)]
    # Build iteratively 
    for i in range(n+1):
        for j in range(i+1):
            if j != 0 and j != i:
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    return ans[n][k]

print(f'recursive ans = {pascalTriangleRecursive(5,2)}')
print(f'top-down ans = {pascalTriangleTopDown(5,2)}')
print(f'bottom-up ans = {pascalTriangleBottomUp(5,2)}')
