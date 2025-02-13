import sys
import math

# def parse_data():
#     sys.stdin = open('input.txt')
#     matrix = []
#     init = False
#     for line in sys.stdin.readlines():
#         if not init:
#             init = True
#             N, M = map(int, line.split())                                
#         else:
#             matrix.append(list(map(int, line.split())))
#             if len(matrix) == N:            
#                 yield N, M, matrix
#                 matrix = []
#                 init = False
                
def parse_data():
    sys.stdin = open('input.txt')
    while True:
        try:
            N, M = map(int, input().split())
            
            matrix = []
            for _ in range(N):
                matrix.append(list(map(int, input().split())))
            
            yield N, M, matrix  
        except EOFError:
            break

def combination(data, k, comb=[], idx=0):
    if len(comb) == k:
        yield comb
    for i in range(idx, len(data)):
        yield from combination(data, k, comb + [data[i]], idx=i+1)
        
def queryMatrix(matrix, query):
    N = len(matrix)
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == query:
                yield r,c


def solve(N, M, matrix):
    chickens = [chicken for chicken in queryMatrix(matrix, 2)]
    area_min = math.inf
    for comb in combination(chickens, M):
        sum = 0
        for house in queryMatrix(matrix, 1):
            house_min = math.inf        
            for chicken in comb:
                dist = distance(house, chicken)                
                if dist < house_min:
                    house_min = dist    
                                    
            sum += house_min
            
        if sum < area_min:
            area_min = sum
            
    return area_min

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
for t, data in enumerate(parse_data()):
    ans = solve(*data)
    print(ans)