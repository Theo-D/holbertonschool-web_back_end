#!/sur/bin/env python3

"""
10-update_topics.py
"""

from typing import List
from pymongo.collection import Collection


def update_topics(mongo_collection: Collection,
                  name: str,
                  topics: List[str]) -> None:
    """
    Update all documents with a given name to set their topics field.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
