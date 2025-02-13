def lcd(a, b):
    r = a % b
    return b if r == 0 else lcd(b, a % b)

def lcdIter(a,b):
    while b:
        a, b = b, a % b        
    return a

print(lcdIter(60,48))