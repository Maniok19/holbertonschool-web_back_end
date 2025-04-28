#!/usr/bin/env python3
"""
Async Comprehension module
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Async Comprehension module"""
    task = []
    timestart = time.time()
    for _ in range(4):
        task.append(async_comprehension())
    await asyncio.gather(*task)
    timeend = time.time()
    restime = timeend - timestart
    return restime
