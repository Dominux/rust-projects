import random

import python_lib

from benchmark_runner import run_benchmark


A = random.randint(0, 1e+5)
B = random.randint(0, 1e+5)
TIMES = 10000

def python_sum_as_string(a: int, b: int) -> str:
    return str(a + b)

def main():
    run_benchmark(python_sum_as_string, a=A, b=B, times=TIMES)
    run_benchmark(python_lib.sum_as_string, a=A, b=B, times=TIMES)


if __name__ == "__main__":
    main()
