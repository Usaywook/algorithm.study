def btRecur(depth, letter):
    if depth > length-1:
        ans.append(letter)
        return
    
    for char in table[number[depth]]:
        btRecur(depth+1,  letter + char)

def btIter(depth, letter):
    stack = [(depth, letter)]
    ans = []
    while stack:
        depth, letter = stack.pop()
        if depth > length -1:
            ans.append(letter)
            continue
        for char in table[number[depth]]:
            stack.append((depth+1, letter + char))
            
if __name__ == "__main__":
    global number, table, length, ans
    number = "259"
    number = [n for n in number]
    length = len(number)
    table = {'2': ['a','b','c'],'5': ['j','k','l'], '9': ['w','x','y','z']}
    
    ans = []   
    btRecur(0, '')
    print(ans, len(ans))
    
    btIter(0, '')
    print(ans, len(ans))