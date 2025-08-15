#!/usr/bin/env python3

"""
8-all.py -
"""

from typing import List, Dict, Any


def list_all(mongo_collection) -> List[Dict[str, Any]]:
    """
    Return all documents in a collection as a list.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
