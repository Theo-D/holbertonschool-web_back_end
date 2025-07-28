#!/usr/bin/env python3
"""
5-sum_list.py: Contains sum_list()
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float.
    """
    float_sum: float = 0
    for num in input_list:
        float_sum += num
    return float_sum
