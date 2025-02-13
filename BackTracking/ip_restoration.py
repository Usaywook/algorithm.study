def is_valid(cand):    
    if len(cand) == 1:
        return True
    if cand[0] == '0':    
        return False
    if int(cand) > 255:
        return False    
    return True        

def btRecur(remain, level=0, select=''):    
    # point : think when level = 4
    if level > 4:
        return            
    if not remain and level == 4:        
        # print(select[:-1])
        ans.append(select[:-1])
        return    
        
    # point : think when min(4, len(remain) + 1)
    for i in range(1, min(4, len(remain) + 1)):     
        cand = remain[:i]                        
        if is_valid(cand):                        
            btRecur(remain[i:], level+1, select + cand + '.')
                        
data = '200523125'
ans = []
btRecur(data)
print(ans)

data = '200023125'
ans = []
btRecur(data)
print(ans)

data = '222523125'
ans = []
btRecur(data)
print(ans)