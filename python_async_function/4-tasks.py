#!/usr/bin/env python3
"""rock bap dooda diwap diwap diwap"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """rock bap dooda diwap diwap diwap"""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
