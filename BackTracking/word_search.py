def solve():
    """
    time complexity: O(NM4^L)
    space complexity: O(NM+L)

    """
    for i in range(N):
        for j in range(M):
            start = array[i][j]
            if start != query[0]:
                continue                        
            if search(i,j, {(i,j)}, [start]):                    
                return True    
    return False

def search(i, j, visited, select=[], level=1):        
    if level == len(query):
        if ''.join(select) == ''.join(query):                       
            return True
        else:
            return False    
    
    for k in range(4):
        next_i = i + di[k]
        next_j = j + dj[k]
        if (next_i, next_j) in visited:
            continue
        if next_i < 0 or next_i > N-1 or next_j < 0 or next_j > M-1:
            continue
        new_e = array[next_i][next_j]        
        if new_e != query[level]:
            continue                 
        
        # not rollback if call by value
        # if search(next_i, next_j, visited | {(next_i, next_j)}, select + [new_e], level+1):
        #     return True
        
        # rollback if call by reference
        visited.add((next_i, next_j))
        select.append(new_e)
        if search(next_i, next_j, visited, select, level+1):
            return True        
        visited.remove((next_i, next_j))
        select.pop()   
             
        
    return False

di = [-1,1,0,0]
dj = [0,0,-1,1]
array = [['d','b','d','e'],['b','d','c','r'],['s','a','b','c']]
N = len(array)
M = len(array[0])
query = ['s','b','d','c','b']
print(solve())

array = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
N = len(array)
M = len(array[0])
query = "SEE"
print(solve())

array = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
N = len(array)
M = len(array[0])
query = "ABCB"
print(solve())
