def solve():
    """
    O(n*2^{n}) - cache : n = 100 단위 솔루션의 턱걸이
    """
    N = len(letter)
    cache = {}
    
    def dp(idx):
        if idx in cache:
            return cache[idx] 
        remain = letter[idx:] 
        if not remain:
            return True        
        
        ans = False
        for i in range(1, N - idx +1):
            if remain[:i] in wordDict:
                ans |= dp(idx + i)
        cache[idx] = ans
        return ans
    
    ans = False
    for i in range(1, N+1):
        if letter[:i] in wordDict:
            ans |= dp(i)
    return ans

def solveIterReverse():
    N = len(letter)
    # initialize
    memo = [False]*N
    if letter[-1] in wordDict:
        memo[0] = True
        # print(f"F(0) =  C({letter[-1]}) = {memo[0]}")
    
    for i in range(1, N):
        # 뒤에서 i+1 문자
        sub = letter[-i-1:] in wordDict
        # print(f"F({i}) = ", end=" ")
        # print(f"C({letter[-i-1:]})", end=" ")
        for j in range(1,i+1):  
            # 뒤에서 i + 1 번째 인덱스 부터 j 인덱스까지 총 i + 1 - j 문자 -  i 개 부터 1 개 문자까지    
            sub |= memo[j-1] if letter[-i-1:-j] in wordDict else False
            # print(f" | C({letter[-i-1:-j]}) & F({j-1})", end=" ")
        memo[i] = sub 
        # print(f"= {sub}")
    
    # print(memo)       
    return memo[-1] 

def solveIterForward():
    N = len(letter)
    # initialize
    memo = [False] * (N+1)
    memo[0] = True
    
    # 앞에서 i 개 문자를 체크
    for i in range(1, N + 1):        
        # j 는 나눌 위치 
        for j in range(i):
            if memo[j] and letter[j:i] in wordDict:
                memo[i] = True
                break
               
    return memo[N] 

letter = 'nocope'
wordDict = ['e','no','cop']
# letter = "leetcode"
# wordDict = ["leet","code"]
# letter = "applepenapple"
# wordDict = ["apple","pen"]
# letter = "catsandog" 
# wordDict = ["cats","dog","sand","and","cat"]
# letter = "aebbbbs"
# wordDict = ["a","aeb","ebbbb","s","eb"]
print(solve())
print(solveIterReverse())
print(solveIterForward())