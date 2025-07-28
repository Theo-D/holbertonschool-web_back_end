#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

"""
9-element_length.py: Annotate a given function's parameters
and return values with the appropriate types.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Reveives an iterable over a sequence and
    returns a list of tuple of sequence and int
    """
    return [(i, len(i)) for i in lst]
