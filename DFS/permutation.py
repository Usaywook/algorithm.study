from typing import List
from itertools import permutations

def PermutationRecursive(remain: List, select: List=[]):
    # base case
    if not remain:
        # print(f'leaf={select}')
        yield select
        return 
    
    # recursive call
    for i in range(len(remain)):
        # print(f'i={i}, remain={remain}, select={select}')
        yield from PermutationRecursive(remain[:i] + remain[i+1:], select=select + [remain[i]])

def PermutationTownDown(remain: List):
    """
    How to make top-down
    arguments -> stack
    return -> continue
    """
    # define stack 
    stack = [(remain, [])]
    while stack:
        remain, select = stack.pop()
        
        # base case
        if not remain:
            # print(f'leaf={select}')
            yield select
            continue
        
        # save stack 
        # ** popright 는 뒤부터 꺼내기 때문에 stack에 쌓는 순서를 반대로 바꿔야한다.
        for i in reversed(range(len(remain))):
            stack.append((remain[:i] + remain[i+1:], select + [remain[i]]))
            # print(f'i={i}, remain={stack[-1][0]}, select={stack[-1][1]}')

def PermutationBottomUp(elements: List):
    # Step 1: Start with the base case: a single empty permutation
    results = [[]]
    
    # Step 2: Iteratively build permutations by adding one element at a time
    for elem in elements:
        new_results = []
        for perm in results:
            # Insert the new element into every possible position in the existing permutations
            for i in range(len(perm) + 1):
                new_results.append(perm[:i] + [elem] + perm[i:])
                # print(f"i = {i}, perm={perm}, results={new_results}")
        results = new_results  # Update results with new permutations
        
    yield from results
            

def PermutationRecursiveK(remain: List, k, select: List=[]):
    # base case
    if len(select) == k:
        yield select
        return 
    
    # recursive call
    for i in range(len(remain)):
        yield from PermutationRecursiveK(remain[:i] + remain[i+1:], k, select=select + [remain[i]])
        
def CircularPermutation(data: List):
    if not data:
        return
    
    # 첫 번째 원소를 고정
    first = data[0]
    remain = data[1:]
    
    # 나머지 원소들로 순열 생성
    for perm in PermutationRecursive(remain):
        yield [first] + list(perm)


def DuplicatePermutationRecursive(remain: List, k, select: List=[]):
    # base case
    if len(select) == k:
        yield select
        return 
    
    # recursive call
    for i in range(len(remain)):
        yield from DuplicatePermutationRecursive(remain, k, select=select + [remain[i]])
        
data = list(range(1,4))
print("PermutationRecursive:")
for perm in PermutationRecursive(data):
    print(perm)

print("PermutationTownDown:")
for perm in PermutationTownDown(data):
    print(perm)
    
print("PermutationBottomUp:")
for perm in PermutationBottomUp(data):
    print(perm)
    
print("PermutationItertools:")
for perm in permutations(data):
    print(perm)

print("PermutationRecursiveK:")
for perm in PermutationRecursiveK(data, 2):
    print(perm)

print("CircularPermutation:")
for perm in CircularPermutation(data):
    print(perm)

print("DuplicatePermutationRecursive:")
for perm in DuplicatePermutationRecursive(data, 2):
    print(perm)
    
def unique_permutations(data):
    data.sort()  # 정렬하여 중복 처리
    return set(list(permutations(data)))

def unique_permutations_recursive(data, perm=[], used=None):
    if used is None:
        used = [False] * len(data)
    
    if len(perm) == len(data):
        yield perm[:]
        return
    
    for i in range(len(data)):
        # 이미 사용된 원소는 건너뛰기
        if used[i]:
            continue
        # 같은 값을 가진 원소는 처음 등장한 경우만 처리
        if i > 0 and data[i] == data[i - 1] and not used[i - 1]:
            continue
        
        used[i] = True
        perm.append(data[i])
        yield from unique_permutations_recursive(data, perm, used)
        perm.pop()
        used[i] = False

def unique_permutations_iterative(data):
    data.sort()  # 정렬하여 중복 방지
    result = []
    stack = [(data, [])]  # (남은 원소, 현재 순열)
    
    while stack:
        remain, perm = stack.pop()
        if not remain:
            result.append(perm)
        else:
            for i in range(len(remain)):
                if i > 0 and remain[i] == remain[i - 1]:
                    continue
                stack.append((remain[:i] + remain[i+1:], perm + [remain[i]]))
    
    return result

print("UniquePermutationsItertools:")
data = [1, 1, 2]
for perm in unique_permutations(data):
    print(perm)

print("UniquePermutationsRecursive:")
data.sort()  # 정렬하여 중복 처리
for perm in unique_permutations_recursive(data):
    print(perm)

print("UniquePermutationsIterative:")
for perm in unique_permutations_iterative(data):
    print(perm)