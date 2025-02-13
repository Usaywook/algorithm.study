def solve_(n):   
    ans = [] 
    def bt(i, j, letter):    
        # positive exit    
        if i+j == 0:
            ans.append(letter)
            return
        # negative exit
        if i > j:
            return
            
        # open call
        if i > 0:
            bt(i-1, j, letter + '(')
        if j > 0:
        # close call
            bt(i, j-1, letter + ')')
    bt(n-1, n, '(')    
    print(ans)    


def solve(n):    
    cache = {}
    def bt(i, j):      
        # check cache return copied result
        if (i, j) in cache:
            return cache[(i, j)]
        
        # positive exit    
        if i+j == 0:        
            return [""]
        # negative exit
        if i > j:
            return []
                
        res = []    
        # open call
        if i > 0:        
            for sub in bt(i-1, j):
                res.append('(' + sub)
            
        if j > 0:
        # close call        
            for sub in bt(i, j-1):
                res.append(')' + sub)
        
        cache[(i,j)] = res    
        return res
    
    ans = bt(n, n)   
    print(cache) 
    return ans
    
ans = solve(3)
print(ans)