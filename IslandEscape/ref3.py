import sys
sys.stdin = open('./input.txt', "r")
 
def is_condition(curr_x, curr_y, next_x, next_y):
    return max(curr_x, curr_y) >= max(next_x, next_y) and min(curr_x, curr_y) >= min(next_x, next_y)

def rotates(data, k=2):
    stack = [([], 0, set())]
    while stack:
        comb, idx, select  = stack.pop()        
        if len(comb) == k:   
            yield  comb + [data[i] for i in set(range(len(data))) - select]
            continue
        
        for i in range(idx, len(data)):            
            stack.append((comb + [data[i]], i+1, select | {i})) 
            
def solve(array):
    all_paths = []
    
    max_ans = float("-inf")
    for k in range(1, N + 1):
        for i in range(N):        
            # rotate node
            for j, rotate in enumerate(rotates(array[i])):
                stack = [(rotate, {i}, [rotate], rotate[2])]
            
                while stack:
                    curr, visited, path, hieght = stack.pop()        
                    
                    # visit node
                    # print(f"visit node = {path[-1]}, {curr}")
                    # print(f"already visited = {visited}")
                    
                    if len(visited) == k:
                        # visit root
                        # print(f"visit root = {path}, {hieght}")
                        all_paths.append([path]) 
                        if hieght > max_ans:
                            max_ans  = hieght
                        continue
                        
                    # search neighbor
                    for m in range(N):   
                        if m in visited:
                            continue                     
                        for n, next in enumerate(rotates(array[m])):                                 
                            if is_condition(curr[0], curr[1], next[0], next[1]):
                                stack.append((next, visited | {m}, path + [next], hieght + next[2]))
                                                            
    return max_ans


T = int(input())
for t in range(T):
    print(f"#{t}", end=" ")
    N = int(input())
    array = []
    for i in range(N):    
        array.append(list(map(int, input().split())))
    
    # print(N, array)
    ans = solve(array)
    print(ans)