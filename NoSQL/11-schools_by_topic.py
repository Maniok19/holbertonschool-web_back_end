#!/usr/bin/env python3
"""wababa baba baba baba baba"""


def schools_by_topic(mongo_collection, topic):
    """wababa baba baba baba baba"""
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
