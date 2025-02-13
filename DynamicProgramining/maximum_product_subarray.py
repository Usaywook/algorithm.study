def solve(data):
    ans = f_max = f_min = data[0]        
    for i in range(1, len(data)):
        cand = (f_min * data[i], f_max * data[i], data[i])
        f_min = min(cand)
        f_max = max(cand)        
        ans = max(f_max, ans)
    return ans


data = [3,-2,1,0,-8,-9]
print(solve(data))