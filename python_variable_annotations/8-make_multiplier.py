#!/usr/bin/env python3
"""
8-make_multiplier.py: Contains make_multiplier()
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function that multiplies
    a float by multiplier.
    """
    def mult_func(multiplier2: float) -> float:
        return multiplier * multiplier2
    return mult_func
