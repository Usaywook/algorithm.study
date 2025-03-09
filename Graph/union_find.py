def makeSet(keys):
    for k in keys:
        P[k] = k
        # depth를 저장하여 union 호출 시 업데이트하고 find를 선형시간에서 로그시간으로 바꾸기 위한 최적화용
        R[k] = 0
        # 각 set의 child 수를 상수 시간에 구하기 위한 최적화용
        C[k] = 1
    
def find(x):
    return x if P[x] == x else find(P[x])

def union(x, y):    
    x = find(x)
    y = find(y)
    if x == y:
        return
    P[y] = x
    
def findwithPathCompletion(x):
    if P[x] == x:
        return x 
    else:
        # 재귀 호출 시 만나는 모든 부모노드를 root의 child로 만들고 반환
        P[x] = find(P[x])
        return P[x]
        
def unionByRank(x, y):    
    x = findwithPathCompletion(x)
    y = findwithPathCompletion(y)
    if x == y:
        return
    if R[x] < R[y]:
        P[x] = y # x의 루트를 y로
        # set의 노드 수 업데이트 
        C[y] += C[x]
        C[x] = 1
    else:
        P[y] = x # y의 루트를 x로
        if R[x] == R[y]:
            R[x] += 1        
        # set의 노드 수 업데이트 
        C[x] += C[y]
        C[y] = 1
        
nodes = list(range(1,9))

P = {}
R = {}
C = {}
makeSet(nodes)
union(1, 2)
union(4, 5)
union(6, 1)
union(3, 7)
union(7, 8)
union(2, 5)
for v in nodes:
    print(find(v), end=' ')
print()
print(P)

P = {}
R = {}
C = {}
makeSet(nodes)
unionByRank(1, 2)
unionByRank(4, 5)
unionByRank(6, 1)
unionByRank(3, 7)
unionByRank(7, 8)
unionByRank(2, 5)
for v in nodes:
    print(findwithPathCompletion(v), end=' ')
print()
print(P)
print(R)
print(C)
