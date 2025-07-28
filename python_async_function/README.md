# Web Back End - Python Asynchronous Functions
## This directory contains files needed for the project Python - Async Functions

0-basic_async_syntax.py - An asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

1-concurrent_coroutines.py - A function that return the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.

2-measure_runtime.py - A function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay), and returns total_time / n.

3-tasks.py - A function task_wait_random that takes an integer max_delay and returns a asyncio.Task.

4-tasks.py - Similar code to `1-concurrent_coroutines.py` but calling task_wait_random() instead of wait_random().
