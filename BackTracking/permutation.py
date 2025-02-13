from collections import deque

def btref(level=0, select=[]):
    if level == len(data):        
        ans.append(select.copy())
        return
    
    for e in data:
        if e in select:
            continue
        select.append(e)
        # call by reference
        btref(level+1, select)
        select.pop()

def btval(level=0, select=[]):
    if level == len(data):
        ans.append(select)
        return
    
    for e in data:
        if e in select:
            continue        
        # call by value
        btval(level+1, select + [e])

def btit():
    # using dfs -> only call by value
    stack = [(0, [])]
    while stack:
        level, select = stack.pop()    
            
        if level == len(data):            
            ans.append(select)
            continue
        for e in data:
            if e in select: continue            
            stack.append((level+1, select + [e]))             

def btitq():
    # using bfs -> only call by value
    queue = deque()
    queue.append((0, []))
    while queue:
        level, select = queue.popleft()    
            
        if level == len(data):            
            ans.append(select)
            continue
        for e in data:
            if e in select: continue            
            queue.append((level+1, select + [e]))         
            
data = ['a','b','c']
ans = []
btref()
print(ans)

ans = []
btval()
print(ans)

ans = []
btit()
print(ans)

ans = []
btitq()
print(ans)