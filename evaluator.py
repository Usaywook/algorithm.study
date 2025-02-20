import tracemalloc
import sys
import gc
import time

def memory_usage_decorator(func):
    def wrapper(*args, **kwargs):
        # 가비지 컬렉션 수행 후 초기 메모리 상태 저장
        gc.collect()
        tracemalloc.start()
        initial_snapshot = tracemalloc.take_snapshot()
        
        # 실행 시간 측정 시작
        start_time = time.time()
        
        # 함수 실행
        result = func(*args, **kwargs)
        
        # 실행 시간 측정 종료
        end_time = time.time()
        execution_time = end_time - start_time
        
        # 최종 메모리 상태 저장
        final_snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        
        # 힙 메모리 사용량 계산
        initial_stats = {stat.size for stat in initial_snapshot.statistics("lineno")}
        final_stats = {stat.size for stat in final_snapshot.statistics("lineno")}
        heap_memory_used = sum(final_stats) - sum(initial_stats)
        
        # 정적 메모리 사용량 계산 (전역 변수 크기 비교)
        global_vars = {k: v for k, v in globals().items() if not k.startswith("__")}
        static_memory_used = sum(sys.getsizeof(v) for v in global_vars.values())
        
        print(f"Function: {func.__name__}")
        print(f"Heap Memory Used: {heap_memory_used} bytes")
        print(f"Static Memory Used: {static_memory_used} bytes")
        print(f"Total Memory Used: {heap_memory_used + static_memory_used} bytes")
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        return result
    
    return wrapper