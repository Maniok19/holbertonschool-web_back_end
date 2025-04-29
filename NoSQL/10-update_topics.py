#!/usr/bin/env python3
"""wababa baba baba baba baba"""


def update_topics(mongo_collection, name, topics):
    """wababa baba baba baba baba"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
