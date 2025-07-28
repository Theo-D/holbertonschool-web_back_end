# Web Back End - Python Async Comprehension
## This directory contains files needed for the project Python - Async Comprehension

0-async_generator.py - A coroutine that will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.

1-async_comprehension.py - A coroutine that will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.

2-measure_runtime.py - A coroutine that will execute `async_comprehension` 4 times, measure the total runtime and return it.
