from collections import deque

num_to_char = {str(i+1): chr(unicode) for i, unicode in enumerate(range(ord('A'), ord('Z')+1))}

def dpRecur(remain):
    """
    T < O(2^{n+1})
    """            
    if not remain:
        return 1
    
    # first
    cnt = 0
    if remain[:1] in num_to_char:
        cnt += dpRecur(remain[1:])        
    
    # second
    if len(remain) > 1 and remain[:2] in num_to_char:
        cnt += dpRecur(remain[2:])                
    return cnt

def dpRecurMemo(remain, cache={}):  
    if remain in cache:
        return cache[remain]
    if not remain:
        return 1
    
    cnt = 0
    if remain[:1] in num_to_char:
        cnt += dpRecurMemo(remain[1:])        
        
    if len(remain) > 1 and remain[:2] in num_to_char:
        cnt += dpRecurMemo(remain[2:])            
    cache[remain] = cnt
    return cnt

def dpRecurData(remain, cache={}):
    if remain in cache:
        return cache[remain]
    if not remain:
        return [[]]
        
    ans = []
    if remain[:1] in num_to_char:
        for sub in dpRecurData(remain[1:]):
            ans.append([remain[:1]] + sub)
        
    if len(remain) > 1 and remain[:2] in num_to_char:
        for sub in dpRecurData(remain[2:]):
            ans.append([remain[:2]] + sub)
    cache[remain] = ans
    return ans

def dpIter(letter):
    """
    f[n] = condition1 * f[n-1] + condition2 * f[n-2]
    """
    N = len(letter)        
    memo = [0] * N                    
    memo[0] = (letter[-1] in num_to_char) * 1 
    if N > 1:           
        memo[1] = (letter[-2] in num_to_char) * memo[0] + (letter[-2:] in num_to_char) * 1    
    for i in range(2, N):             
        memo[i] = (letter[-i-1:-i] in num_to_char) * memo[i-1] + (letter[-i-1:(-i+1)] in num_to_char) * memo[i-2]                
    return memo[N-1]

def dpIterWindow(letter):
    N = len(letter)        
    memo = deque(maxlen=2)               
    memo.append((letter[-1] in num_to_char) * 1)    
    if N > 1:           
        memo.append((letter[-2] in num_to_char) * memo[0] + (letter[-2:] in num_to_char) * 1)  
        
    for i in range(2, N):             
        memo.append((letter[-i-1:-i] in num_to_char) * memo[1] + (letter[-i-1:(-i+1)] in num_to_char) * memo[0])        
    return memo.pop()

s ="123123"

# ans = dpRecur(s)
# print(ans)
# ans = dpRecurMemo(s)
# print(ans)
# ans = dpRecurData(s)
# print(ans)
ans = dpIter(s)
print(ans)
ans = dpIterWindow(s)
print(ans)
