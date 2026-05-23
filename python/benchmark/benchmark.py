from time import perf_counter
import tracemalloc
import statistics
from functools import wraps


def benchmark(repeats=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # ---- timing pass ----
            times = []

            for _ in range(repeats):
                t0 = perf_counter()
                func(*args, **kwargs)
                times.append(perf_counter() - t0)

            # ---- memory pass ----
            tracemalloc.start()
            func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            result = {
                "time_avg_sec": statistics.mean(times),
                "time_ms_sec": min(times) * 1000,
                "peak_memory_kb": peak / 1024,
            }

            return result

        return wrapper
    return decorator