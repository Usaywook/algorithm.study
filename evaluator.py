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

        # 스택 메모리 측정을 위한 초기 스택 깊이 측정 함수
        def get_depth():
            depth = 0
            frame = sys._getframe()
            while frame:
                depth += 1
                frame = frame.f_back
            return depth

        initial_depth = get_depth()
        current_depth = [initial_depth]  # 리스트로 감싸서 mutable하게 관리
        max_depth = [initial_depth]

        # 프로파일러 함수: 함수 호출 시 스택 깊이를 추적
        def tracefunc(frame, event, arg):
            if event == 'call':
                current_depth[0] += 1
                if current_depth[0] > max_depth[0]:
                    max_depth[0] = current_depth[0]
            elif event == 'return':
                current_depth[0] -= 1
            return tracefunc

        # 스택 깊이 측정을 위해 프로파일러 활성화
        sys.setprofile(tracefunc)

        # 함수 실행
        result = func(*args, **kwargs)

        # 프로파일러 비활성화
        sys.setprofile(None)

        # 실행 시간 측정 종료
        end_time = time.time()
        execution_time = end_time - start_time

        # 최종 메모리 상태 저장 (힙 메모리 측정)
        final_snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()

        # 힙 메모리 사용량 계산 (라인별 메모리 할당)
        initial_stats = {stat.size for stat in initial_snapshot.statistics("lineno")}
        final_stats = {stat.size for stat in final_snapshot.statistics("lineno")}
        heap_memory_used = sum(final_stats) - sum(initial_stats)

        # 정적 메모리 사용량 계산 (전역 변수의 크기)
        global_vars = {k: v for k, v in globals().items() if not k.startswith("__")}
        static_memory_used = sum(sys.getsizeof(v) for v in global_vars.values())

        # 스택 메모리 사용량 계산 (추정)
        depth_increase = max_depth[0] - initial_depth
        avg_frame_size = sys.getsizeof(sys._getframe())
        stack_memory_used = depth_increase * avg_frame_size

        print(f"Function: {func.__name__}")
        print(f"Heap Memory Used: {heap_memory_used} bytes")
        print(f"Static Memory Used: {static_memory_used} bytes")
        print(f"Stack Memory Used (estimated): {stack_memory_used} bytes")
        total_memory_used = heap_memory_used + static_memory_used + stack_memory_used
        print(f"Total Memory Used: {total_memory_used / 1000:.0f} kb")
        print(f"Execution Time: {execution_time * 1000:.0f} ms")

        return result

    return wrapper