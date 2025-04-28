#!/usr/bin/env python3
"""Async Comprehension module blabla blabl blabla blabl blabl"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """Async Comprehension module blabla blabl blabla blabl blabl"""
    lif = []
    async for i in async_generator():
        lif.append(i)
    return lif
