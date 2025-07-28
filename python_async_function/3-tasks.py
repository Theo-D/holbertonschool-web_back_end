#!/usr/bin/env python3
"""
3-tasks.py: Contains definition of task_wait_random().
"""
from asyncio import Task, create_task


def task_wait_random(max_delay: int) -> Task:
    """
    A function that return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    return create_task(wait_random(max_delay))
