#!/usr/bin/env python3
"""wababa baba baba baba baba"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    if mongo_collection is None:
        return []
    result = list(mongo_collection.find())
    return result
