#!/usr/bin/env python3
"""
9-element_length.py: Annotate a given function's parameters
and return values with the appropriate types.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Reveives an iterable over a typing.sequence and
    returns a list of tuple of typing.sequence and int
    """
    return [(i, len(i)) for i in lst]
