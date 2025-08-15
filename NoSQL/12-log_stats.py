#!/usr/bin/env python3
"""
12-log_stats.py -
Script providing statistics about Nginx logs stored in MongoDB.
Counts documents by retrieving them with find() and counting in Python.
"""

from typing import Any
from pymongo.collection import Collection
from pymongo import MongoClient


def count_documents_by_find(collection: Collection, filter_query: dict) -> int:
    """Count documents by fetching them and counting locally."""
    cursor = collection.find(filter_query)
    return len(list(cursor))


def main() -> None:
    """
    Connects to MongoDB, retrieves statistics about logs using find(),
    and prints counts for total logs, HTTP methods, and status checks.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection: Collection = client.logs.nginx

    total_logs = len(list(nginx_collection.find()))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        count = count_documents_by_find(nginx_collection, {"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = count_documents_by_find(nginx_collection, {"path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
