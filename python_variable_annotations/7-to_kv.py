#!/usr/bin/env python3

"""
to_kv: A  type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple..
"""


def to_kv(k: str, v: int | float) -> tuple[str, int | float]:
    v_squared: float = v * v
    new_tuple: tuple[str, int | float] = (k, v_squared)
    return new_tuple
