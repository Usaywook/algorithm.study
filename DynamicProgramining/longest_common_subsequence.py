def solve1(text1, text2):
    cache = {}
    def dp(m, n):
        if (m,n) in cache:
            return cache[(m,n)]
        if m==0 or n==0:
            return 0
        
        ans = dp(m-1, n-1) + 1 if text1[m-1] == text2[n-1] else max(dp(m-1, n), dp(m, n-1))                
        cache[(m,n)] = ans
        return ans
    
    return dp(len(text1), len(text2))

def solve2(text1, text2):
    M = len(text1)
    N = len(text2)
    memo = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1,M+1):
        for j in range(1,N+1):                        
            memo[i][j] = memo[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(memo[i-1][j], memo[i][j-1])
    return memo[M][N]

text1 = 'abdcg'
text2 = 'bdg'

print(solve1(text1, text2))
print(solve2(text1, text2))