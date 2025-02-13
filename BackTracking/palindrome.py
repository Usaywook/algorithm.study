def solve(letter):        
    cache = {}    
    def isValid(char):        
        N = len(char)
        for i in range(N // 2):
            if char[i] != char[N-1-i]:
                return False
        return True        

    def bt(remain):    
        if remain in cache:
            return cache[remain]
        if not remain:                    
            return [[]]        
        ans = []
        for i in range(1, len(remain)+1):
            char = remain[:i]
            if not isValid(char):
                continue        
            for sub in bt(remain[i:]):                
                ans.append([char] + sub)        
        cache[remain] = ans
        return ans    
    
    return bt(letter)

letter = "aabb"
print(solve(letter))