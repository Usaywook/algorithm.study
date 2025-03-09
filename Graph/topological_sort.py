from collections import deque

graph = {
    0: [1],
    1: [2],
    2: [5],
    3: [0, 4],
    4: [1, 2],    
    5: []
}

def sortWithBFS():
    in_degree = [0]*len(graph.keys())
    for k, v in graph.items():
        for e in v:
            in_degree[e] += 1

    visited = [False]*len(in_degree)
    ans = []
    Q = deque()
    for i, x in enumerate(in_degree):
        if x == 0:
            visited[i] = True
            Q.append(i)      

    while Q:
        i = Q.popleft()
        ans.append(i)
        
        for j in graph[i]:
            if not visited[j]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    visited[j] = True
                    Q.append(j)
    return ans

def sortWithDFSRecursive():
    ans = []
    visited = [False] * len(graph.keys())
    for i in graph.keys():
        
        def dfs(u):
            visited[u] = True
            
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)          
                                   
            ans.append(u)
            
        if not visited[i]:
            dfs(i)
            
    return list(reversed(ans))
                                

def sortWithDFSIteractive():
    ans = []
    visited = [False] * len(graph.keys())
    for i in graph.keys():
        tmp = []            
        if not visited[i]:
            stack = [i]
            while stack:
                u = stack.pop()
                visited[u] = True
                for v in graph[u]:
                    if not visited[v]:
                        stack.append(v)
            
                tmp.append(u)
        ans = tmp + ans                
            
    return ans

print(sortWithBFS())
print(sortWithDFSRecursive())
print(sortWithDFSIteractive())

graph = {
    0: [6],
    1: [2, 4, 6],
    2: [],
    3: [0, 4],
    4: [],    
    5: [1],
    6: [],
    7: [0, 1]
}

print(sortWithBFS())
print(sortWithDFSRecursive())
print(sortWithDFSIteractive())