import sys
sys.stdin = open('input.txt', 'r')

import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from evaluator import memory_usage_decorator


@memory_usage_decorator
def solve():
    def isChargable(x, y, charge):
        if abs(x - charge[0]) + abs(y - charge[1]) <= charge[2]:
            return True
        return False

    T = int(input())
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]
    for test_case in range(1, T + 1):
        M, A = map(int, input().split())
        move_A = list(map(int, input().split()))
        move_B = list(map(int, input().split()))
        chargers = []
        for _ in range(A):
            x, y, c, p = map(int, input().split())
            chargers.append([x, y, c, p])
        
        def search(x_A, y_A, x_B, y_B, t=0, total=0, charge_A=[], charge_B=[]): 
            if t == M + 1:
                # print(f"charge_A: {charge_A}, sum_A : {sum(charge_A)}")
                # print(f"charge_B: {charge_B}, sum_B : {sum(charge_B)}")
                return total
                
            d_A = move_A[t-1] if t != 0 else 0        
            nx_A = x_A + dx[d_A]
            ny_A = y_A + dy[d_A]        
            
            d_B = move_B[t-1] if t != 0 else 0
            nx_B = x_B + dx[d_B]
            ny_B = y_B + dy[d_B]
            
            max_charge = 0
            max_charge_A, max_charge_B = 0, 0         
            for i, charger_A in enumerate(chargers):
                for j, charger_B in enumerate(chargers):
                    p_A = charger_A[3] if isChargable(nx_A, ny_A, charger_A) else 0
                    p_B = charger_B[3] if isChargable(nx_B, ny_B, charger_B) else 0
                    # 두번째 조건을 놓치면 edge case에서 오류가 발생하므로 주의하자.
                    if i == j and p_A == p_B != 0:
                        p_A = p_A // 2
                        p_B = p_B // 2                    
                    charge = p_A + p_B
                    if charge > max_charge:                    
                        max_charge = charge
                        max_charge_A, max_charge_B = p_A, p_B              
            return search(nx_A, ny_A, nx_B, ny_B, t+1, total + max_charge, charge_A + [max_charge_A], charge_B + [max_charge_B])
        
        total = search(1, 1, 10, 10)
        print(f"#{test_case} {total}")
    
solve()