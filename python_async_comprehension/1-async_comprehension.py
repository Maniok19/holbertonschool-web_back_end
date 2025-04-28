#!/usr/bin/env python3
"""
Async Comprehension module
"""
async_generator = __import__('0-async_generator').async_generator
import typing


async def async_comprehension() -> list:
    """
    Collects 10 random numbers using async comprehension
    Returns: List of 10 random float numbers
    """
    lif = []
    async for i in async_generator():
        lif.append(i)
    return lif
