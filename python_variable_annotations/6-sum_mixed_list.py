#!/usr/bin/python3
from typing import Union

"""
sum_mixed_list: A type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    mixed_sum: float = 0
    for num in mxd_lst:
        mixed_sum += num
    return mixed_sum
