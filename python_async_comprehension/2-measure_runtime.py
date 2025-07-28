#!/usr/bin/env python3
"""
2-measure_runtime: Contains defiunition for measure_runtime().
"""
from asyncio import gather
from time import perf_counter


async def measure_runtime() -> float:
    """
    A coroutine that will execute `async_comprehension` 4 times,
    measure the total runtime and return it.
    """
    async_comprehension = __import__(
        '1-async_comprehension'
        ).async_comprehension
    start = perf_counter()

    await gather(*(async_comprehension() for _ in range(4)))

    end = perf_counter() - start

    return end
