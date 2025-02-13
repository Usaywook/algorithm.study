from itertools import combinations, combinations_with_replacement

def combinationRecursive(data, k):
    """
    using back tracking
    data : List of remained data
    k : The number of remained elements 
    """
    # base case 1: all elements are selected
    if k == 0:
        # print("base 1")
        return [[]]
    # base case 2: not any elements are remained
    if not data:
        # print("base 2")
        return []
    
    
    # select first element: c[n-1][k-1] 
    with_first = [[data[0]] + comb for comb in combinationRecursive(data[1:], k-1)]
    
    # not select first element: c[n-1][k]
    without_first = combinationRecursive(data[1:], k)
    
    # print(with_first + without_first)
    return with_first + without_first     

def combinationDFS(data, k, comb=[], idx=0):
    """
    using graph search
    data: 모든 원소들
    k: 선택할 원소 수
    comb: 선택된 조합
    idx: 중복선택을 방지하기 위한 시작 인덱스
    """
    if len(comb) == k:
        yield comb
        return
    
    for i in range(idx, len(data)):
        # 방문한 노드 제외 나머지 인덱스 방문 -> permutation과의 차이
        yield from combinationDFS(data, k, comb=comb + [data[i]], idx=i+1)

def combinationIterative(data, k):
    """
    stack = [(comb: List, idx: int)]
    slice(idx:) 중 1 개 요소의 선택을 k depth까지 진행 
    """
    stack = [([], 0)]
    while stack:
        comb, idx = stack.pop()
        
        # base
        if len(comb) == k:
            yield comb
            continue
        
        for i in range(idx, len(data)):            
            stack.append((comb + [data[i]], i+1))   
            
def combinationWithReplacement(data, k, comb=[], idx=0):
    """
    H(n,k)=C(n+k-1,k)
    """
    if len(comb) == k:
        yield comb
        return

    for i in range(idx, len(data)):  # idx부터 시작하여 중복 선택 허용
        yield from combinationWithReplacement(data, k, comb + [data[i]], idx=i)
        
data = list(range(1,4))
k = 2
print("combinationRecursive")
for comb in combinationRecursive(data, 2):
    print(comb)
print("combinationDFS")
for comb in combinationDFS(data, 2):
    print(comb)
print("combinationIterative")
for comb in combinationIterative(data, 2):
    print(comb)
print("combinationWithItertools")
for comb in combinations(data, 2):
    print(comb)
    
print("combinationWithReplacement")
for comb in combinationWithReplacement(data, 2):
    print(comb)
print("combinationWithReplacementnWithItertools")
for comb in combinations_with_replacement(data, 2):
    print(comb)

