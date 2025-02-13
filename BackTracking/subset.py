def btRecur(level, letter):
    if level == len(data):
        ans.append(letter)
        return
    char = data[level]
    # call by value
    btRecur(level+1, letter + char) 
    btRecur(level+1, letter)

def btIter(level, letter):
    stack = [(level, letter)]
    while stack:
        level, letter = stack.pop()
        if level == len(data):
            ans.append(letter)
            continue
        char = data[level]
        stack.append((level+1, letter+char))
        stack.append((level+1, letter))
        
if __name__ == "__main__":
    global data, ans   
    data = ['a','b','c']
    
    ans = []
    btRecur(0, '')
    print(ans)
    
    ans =[]
    btIter(0, '')
    print(ans)
    
    