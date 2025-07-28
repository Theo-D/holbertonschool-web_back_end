#!/usr/bin/env python3
from typing import Union

"""
6-sum_mixed_list.py: Contains sum_mixed_list()
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """
    A type-annotated function sum_mixed_list which takes a list
    mxd_lst of integers and floats and returns their sum as a float.
    """
    mixed_sum: float = 0
    for num in mxd_lst:
        mixed_sum += num
    return mixed_sum
