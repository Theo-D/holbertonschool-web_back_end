# Web back-end - NoSQL
## This directory contains task files for the NOSQL project.

- **0-list_databases**
  A script that lists all MongoDB databases.

- **3-all**
  A script that lists all documents in the `school` collection of a given database.

- **4-match**
  A script that lists all documents with `name="Holberton school"` in the `school` collection.

- **5-count**
  A script that displays the number of documents in the `school` collection.

- **6-update**
  A script that adds a new attribute `address` with value `"972 Mission street"` to all documents with `name="Holberton school"`.

- **7-delete**
  A script that deletes all documents with `name="Holberton school"` from the `school` collection.

- **8-all.py**
  A Python function `list_all(mongo_collection)` that returns all documents in a given MongoDB collection.

- **9-insert_school.py**
  A Python function `insert_school(mongo_collection, **kwargs)` that inserts a new document with the provided fields into a collection and returns the new document’s `_id`.

- **10-update_topics.py**
  A Python function `update_topics(mongo_collection, name, topics)` that updates the `topics` list of a school document identified by its `name`.

- **11-schools_by_topic.py**
  A Python function `schools_by_topic(mongo_collection, topic)` that returns a list of schools having a specific topic.

- **12-log_stats.py**
  A Python script that connects to the `logs` database and `nginx` collection to display various statistics about Nginx logs, including counts of HTTP methods and status checks.
