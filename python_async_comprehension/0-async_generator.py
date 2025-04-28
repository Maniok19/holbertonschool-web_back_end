#!/usr/bin/env python3
"""
Async Comprehension module
"""
import asyncio
import random


async def async_generator():
    """Async Comprehension module"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
