#!/usr/bin/env python3
"""
1-async_comprehension.py: Contains the function async_comprehension()
"""
from typing import AsyncGenerator, Callable, List


async def async_comprehensionr() -> List[float]:
    """
    A coroutine that will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers.
    """
    async_generator: Callable[[], AsyncGenerator[float, None]] = __import__(
        '0-async_generator'
        ).async_generator
    yielded_res = [i async for i in async_generator()]
    return yielded_res
