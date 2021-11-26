import time
from typing import Callable


def run_benchmark(fn: Callable, times: int, *args, **kwargs) -> None:
    min_score = None

    for _ in range(100):

        start_time = time.perf_counter()
        for t in range(times):
            fn(*args, **kwargs)
        end_time = time.perf_counter()

        # Setting min_score
        if not min_score:
            min_score = end_time - start_time
        elif (new_min_score := end_time - start_time) < min_score:
            min_score = new_min_score

    print(f"{min_score} is min score for {fn.__name__} for {times} times")
