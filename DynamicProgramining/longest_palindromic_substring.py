def solve(letter):
    N = len(letter)    
    # initialize
    max_length = 1
    key = (0, 0)
    memo = [[0]*N for _ in range(N)] 
    for k in range(2):
        for i in range(N - k):
            j = i + k             
            if i == j:
                memo[i][j] = 1             
            else:
                if letter[i] == letter[j]:
                    memo[i][j] = 2 
                    if memo[i][j] > max_length:
                        max_length = memo[i][j]
                        key = (i, j)
                else:
                    memo[i][j] = 0
    
    for k in range(2, N):                
        for i in range(N - k):                        
            j = i + k            
            if memo[i+1][j-1] > 0 and letter[i] == letter[j]:
                memo[i][j] = memo[i+1][j-1] + 2                                            
                if memo[i][j] > max_length:
                    max_length = memo[i][j]
                    key = (i, j)
            else:
                memo[i][j] = 0

    # for i in range(N):
    #     print(memo[i])
    return letter[key[0]:key[1]+1]

def solveOpt(letter):
    N = len(letter)    
    # initialize
    max_length = 1
    key = (0, 0)
    
    memo_even = [1]*N
    memo_odd = [0]*(N-1)
        
    for i in range(N - 1):
        j = i + 1        
        if letter[i] == letter[j]:
            memo_odd[i] = 2 
            if memo_odd[i] > max_length:
                max_length = memo_odd[i]
                key = (i, j)        
    
    for k in range(2, N):                
        for i in range(N - k):                        
            j = i + k     
            memo = memo_even if k % 2 == 0 else memo_odd            
            if memo[i+1] > 0 and letter[i] == letter[j]:
                memo[i] = memo[i+1] + 2                                            
                if memo[i] > max_length:
                    max_length = memo[i]
                    key = (i, j)
            else:
                memo[i] = 0

    return letter[key[0]:key[1]+1]


# letter = "a"
# letter = "aacabdkacaa"
# letter = "babad"
letter =  "cbbd"
print(solve(letter))
