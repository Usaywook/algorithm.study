import sys

def SolveRecursive(words, depth=0, alphabets=set()):
    N = len(words)
    
    # base case
    if depth == N:
        if len(alphabets) == 26:
            return 1
        return 0
    
    # not use case
    ans1 = SolveRecursive(words, depth=depth+1, alphabets=alphabets)
    
    # use case 
    ans2 = SolveRecursive(words, depth=depth+1, alphabets=alphabets | words[depth])
    
    return ans1 + ans2
    
def SolveTopDown(words):
    N = len(words)
    cnt = 0
    stack = [(0, set())]
    
    while stack:
        depth, alphabets = stack.pop()
        
        # base case
        if depth == N:
            if len(alphabets) == 26:
                cnt += 1
        else:
            # not use case
            stack.append((depth+1, alphabets))    
                            
            # use case
            stack.append((depth+1, alphabets | words[depth]))
        
    return cnt
    
sys.stdin = open('sample_input.txt')
T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    print(f'#{t+1}', end=' ')
    words = []
    for i in range(N):
        word = str(sys.stdin.readline().strip())
        words.append(set(alphabet for alphabet in word))
    ans_recursive = SolveRecursive(words)
    print(ans_recursive)
    
    ans_topdown = SolveTopDown(words)
    assert ans_recursive == ans_topdown