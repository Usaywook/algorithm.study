def btRecur(level, remain, res, select=[]):
    # base 
    if sum(select) == target:        
        ans.append(select)
        return
    
    # process
    for i in range(len(remain)):
        choice = remain[i]
        query = res - choice
        if query < 0:
            continue
        # call
        btRecur(level+1, remain[i:], query, select + [choice])

def btIter(level, remain, res, select=[]):
    stack = [(level, remain, res, select)]
    while stack:
        level, remain, res, select = stack.pop()
        if sum(select) == target:        
            ans.append(select)
            continue
        for i in range(len(remain)):
            choice = remain[i]
            query = res - choice
            if query < 0:
                continue
            stack.append((level+1, remain[i:], query, select + [choice]))


global data, target
data = [1,2,3]
target = 5

ans = []
btRecur(0, data, target)
print(ans)

ans = []
btIter(0, data, target)
print(ans)