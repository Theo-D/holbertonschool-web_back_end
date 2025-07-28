#!/usr/bin/env python3
"""
2-measure_runtime.py: Contains definition of measure_time().
"""
from typing import Awaitable, Callable
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    A function with integers n and max_delay as arguments that measures the
    total execution time for wait_n(n, max_delay), and returns total_time / n.
    """
    wait_n: Callable[[int, int], Awaitable[float]] = __import__(
        '1-concurrent_coroutines'
        ).wait_n
    start: float = time.perf_counter()
    wait_n(n, max_delay)
    total: float = time.perf_counter() - start

    return total / n
