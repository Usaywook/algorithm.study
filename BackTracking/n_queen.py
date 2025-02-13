visited_col = set()
visited_diag_sum = set()
visited_diag_min = set()

def getCand(i):
    cand = []
    for j in range(N):
        if isValid(i,j):
            cand.append(j)
    return cand

def isValid(i, j):
    if j in visited_col:        
        return False
    if i+j in visited_diag_sum:        
        return False
    if i-j in visited_diag_min:        
        return False    
    return True
            
def bt(row):
    # positive leaf
    if row == N:        
        all_ans.append([''.join(x) for x in ans])                
        return
    # negative leaf
    cand = getCand(row)
    if len(cand) == 0:                
        return
    
    for col in cand:        
        ans[row][col] = 'Q'
        visited_col.add(col)
        visited_diag_sum.add(row+col)
        visited_diag_min.add(row-col)        
        bt(row+1)        
        ans[row][col] = '.'
        visited_col.remove(col)
        visited_diag_sum.remove(row+col)
        visited_diag_min.remove(row-col)
    
def solve():        
    bt(0)    
    print(all_ans)

N = 4
all_ans = []
ans = [['.' for _ in range(N)] for _ in range(N)]
solve()