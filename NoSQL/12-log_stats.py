#!/usr/bin/env python3
"""
12-log_stats.py -
"""

from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Total logs count
    total_logs = collection.count_documents({})

    # HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Print the stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
