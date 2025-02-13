def prime_factorization_recursive(n):
    """Top-Down 방식으로 재귀적으로 소인수 분해"""        
    if n == 1:  # 1의 경우 소인수 없음
        return []    
    # 가장 작은 소인수 찾기
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # i가 소인수이면            
            return [i] + prime_factorization_recursive(n // i)  # 재귀 호출 후 반환            
    # 소수인 경우 자기 자신을 반환    
    return [n]

def prime_factorization_recursive_memo(n, dp={}):
    """Top-Down 방식으로 재귀적으로 소인수 분해 (Memoization 적용)"""
    if n in dp:  # 이미 계산된 경우, 저장된 값을 반환
        return dp[n]
    
    if n == 1:  # 1의 경우 소인수 없음
        return []

    # 가장 작은 소인수 찾기
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # i가 소인수이면
            dp[n] = [i] + prime_factorization_recursive_memo(n // i, dp)  # 재귀 호출 후 저장
            return dp[n]
    
    # 소수인 경우 자기 자신을 반환
    dp[n] = [n]
    return dp[n]

def sieve_spf(n):
    """1부터 n까지의 숫자의 가장 작은 소인수(SPF)를 미리 계산하는 함수"""
    spf = list(range(n + 1))  # 초기값: 자기 자신으로 설정
    
    for i in range(2, int(n**0.5) + 1):  # 2부터 √N까지
        if spf[i] == i:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수들을 처리
                if spf[j] == j:  # 아직 갱신되지 않은 경우만 갱신
                    spf[j] = i  
                    
    return spf  # 소인수 테이블 반환

def sieve_spf_linear(n):
    """O(N) 시간복잡도로 가장 작은 소인수(SPF) 테이블을 생성하는 알고리즘"""
    spf = list(range(n + 1))  # 초기값: 자기 자신을 소인수로 설정
    primes = []  # 발견한 소수 리스트
    
    for i in range(2, n + 1):
        if spf[i] == i:  # i가 소수이면
            primes.append(i)  # 소수 리스트에 추가

        # 현재 소수 리스트를 이용해 i의 배수를 처리
        for prime in primes:
            if prime * i > n:  # 범위를 초과하면 중단
                break
            spf[prime * i] = prime  # 가장 작은 소인수 갱신
            
            if i % prime == 0:  # i가 prime의 배수이면, 이후 배수는 이미 처리됨
                break
    
    return spf

def prime_factorization(n, spf):
    """DP로 미리 계산한 SPF 테이블을 이용하여 빠르게 소인수 분해"""
    factors = []
    while n != 1:
        factors.append(spf[n])
        n //= spf[n]
    return factors

# 실행 예시
# 특정 숫자의 소인수 분해
print(prime_factorization_recursive(84))  # 출력: [2, 2, 3, 7]
print(prime_factorization_recursive(75))  # 출력: [3, 5, 5]

print(prime_factorization_recursive_memo(84))  # 출력: [2, 2, 3, 7]
print(prime_factorization_recursive_memo(75))  # 출력: [3, 5, 5]

N = 100  # 1부터 100까지 미리 계산
spf = sieve_spf_linear(N)
print(prime_factorization(84, spf))  # 출력: [2, 2, 3, 7]
print(prime_factorization(75, spf))  # 출력: [3, 5, 5]