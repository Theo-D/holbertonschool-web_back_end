#!/usr/bin/env python3
"""
0-simple_helper_function.py - A helper function that returns a tuple of size
two containing a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range: receives two pos ints and calculates corresponding
    start and end indexes returned as a tuples
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    tuple_range = (start_index, end_index)

    return tuple_range
