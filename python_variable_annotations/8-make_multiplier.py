#!/usr/bin/env python3
from typing import Callable

"""
make_multiplier: A type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that multiplies
a float by multiplier.
"""


def make_multiplier(mutiplier: float) -> Callable[[float], float]:
    def mult_func(multiplier2: float) -> float:
        return mutiplier * multiplier2
    return mult_func
