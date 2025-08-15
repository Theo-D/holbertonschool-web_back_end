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

    total_logs = count_documents_by_find(nginx_collection, {})
    get_count = count_documents_by_find(nginx_collection, {"method": "GET"})
    post_count = count_documents_by_find(nginx_collection, {"method": "POST"})
    put_count = count_documents_by_find(nginx_collection, {"method": "PUT"})
    patch_count = count_documents_by_find(nginx_collection, {"method": "PATCH"})
    delete_count = count_documents_by_find(nginx_collection, {"method": "DELETE"})
    status_count = count_documents_by_find(nginx_collection, {"path": "/status"})

    print('{} logs'.format(total_logs))
    print('Methods:')
    print('\tmethod GET: {}'.format(get_count))
    print('\tmethod POST: {}'.format(post_count))
    print('\tmethod PUT: {}'.format(put_count))
    print('\tmethod PATCH: {}'.format(patch_count))
    print('\tmethod DELETE: {}'.format(delete_count))
    print('{} status check'.format(status_count))


if __name__ == "__main__":
    main()
