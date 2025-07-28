#!/usr/bin/env python3
"""
7-to_kv.py: Contains to_kv()
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    A type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple.
    """
    v_squared: float = v * v
    new_tuple: Tuple[str, Union[int, float]] = (k, v_squared)
    return new_tuple
