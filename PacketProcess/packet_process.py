def search(cpu_num, i, packets, processes, queues):
    # 모든 패킷까지 조건 만족
    if i > len(packets) - 1:        
        return True
            
    time, length = packets[i]
    
    # 즉각 처리 경우     
    for cpu in range(cpu_num):
        cpu_time = processes[cpu]
        # 즉각처리 불가한 경우 제외
        if cpu_time > time:
            continue                    
        processes[cpu] = time + length 
        # call left node
        if search(cpu_num, i+1, packets, processes, queues):
            return True 
        # rollback
        processes[cpu] = cpu_time
        break    
        
    
    # 큐 대기 경우    
    min_length = 11    
    min_cpu = -1                  
    for cpu in range(cpu_num):     
        cpu_time = processes[cpu]
        # 즉각처리 가능한 경우 제외
        if cpu_time <= time:
            continue  
        
        # 총 처리시간 계산
        packet_length = cpu_time - time + length
        for queue_length in queues[cpu]:
            packet_length += queue_length
        if min_length > packet_length:
            min_length = packet_length
            min_cpu = cpu
            
    # call right node    
    if min_cpu != -1 and min_length <= 10: 
        queues[min_cpu].append(length)            
        if search(cpu_num, i+1, packets, processes, queues):
            return True
        # rollback
        queues[min_cpu].pop()
       
    return False
    
def solve():
    N = int(input())    
    packets = []
    for _ in range(N):
        packets.append(tuple(map(int, input().split())))
    
    for cpu_num in range(1, 6):
        processes = {i: 0 for i in range(cpu_num)}
        queues  = {i: [] for i in range(cpu_num)}
        time, length = packets[0]
        processes[0] = time + length
        if search(cpu_num, 1, packets, processes, queues):
            return cpu_num        
    
    return -1

if __name__ == '__main__':
    import sys
    sys.stdin = open("input.txt", 'r')

    T = int(input())
    for t in range(1, T+1):
        print(f"#{t}", end=" ")
        ans = solve()
        print(ans)