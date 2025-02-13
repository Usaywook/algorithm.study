import math

matrix = [[2,4,3],[1,3,7],[6,5,6]]
output = [11, 14, 11, 17, 9, 12]


def solve(matrix):
    N = len(matrix) 
    # min = float('inf')
    min = math.inf
    for perm in permute(list(range(N))):
        sum = 0
        for row, col in enumerate(perm):
            elem = matrix[row][col]
            # print(row, col, elem)
            sum += elem
        print(sum, end=" ")
        if sum < min:
            min = sum
    print()
    return min
            
def permute(remain, select=[], row=0):
    if not remain:
        yield select
        return
    
    for i in range(len(remain)):
        yield from permute(remain[:i] + remain[i+1:], select + [remain[i]])
    

print(solve(matrix))