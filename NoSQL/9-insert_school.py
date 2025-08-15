#!/usr/bin/env python 3

"""
9-insert_school.py -
"""

from typing import Any
from pymongo.collection import Collection
from bson.objectid import ObjectId


def insert_school(mongo_collection: Collection, **kwargs: Any) -> ObjectId:
    """
    Insert a new document in the collection and return its _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
