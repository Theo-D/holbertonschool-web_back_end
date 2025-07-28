#!/usr/bin/env python3
"""
0-async_generator.py: Contains the function async_generator()
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    A coroutine that will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
