#!/usr/bin/env python3

"""
sum_list: A type-annotated function sum_list which takes a list input_list
 of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    float_sum: float = 0
    for num in input_list:
        float_sum += num
    return float_sum
