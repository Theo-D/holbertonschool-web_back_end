#!/usr/bin/env python3
"""
4-tasks.py: Contains definition of task_wait_n().
"""
from typing import List, Awaitable, Callable
from asyncio import as_completed


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A function that return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    task_wait_random: Callable[[int], Awaitable[float]] = __import__(
        '3-tasks'
        ).task_wait_random
    delay_list: List[float] = []

    tasks: List[Awaitable[float]] = [task_wait_random(max_delay)
                                     for _ in range(n)]

    for task in as_completed(tasks):
        delay: float = await task
        delay_list.append(delay)

    return delay_list
