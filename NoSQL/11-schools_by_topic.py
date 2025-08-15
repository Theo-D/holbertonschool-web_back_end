#!/usr/bin/env python3
"""
11-school_by_topics.py -
"""

from typing import List, Dict, Any
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection,
                     topic: str) -> List[Dict[str, Any]]:
    """
    Return a list of schools that have the given topic in their topics list.
    """
    return list(mongo_collection.find({"topics": topic}))
