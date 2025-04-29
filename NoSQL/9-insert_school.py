#!/usr/bin/env python3
"""wababa baba baba baba baba"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
