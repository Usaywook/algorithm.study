def lcd(a,b):    
    return a if b == 0 else lcd(b, a%b) 
def gcm(a,b):
    return int(a*b / lcd(a,b))

print(gcm(60,48))