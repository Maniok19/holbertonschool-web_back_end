#!/usr/bin/env python3
"""rock bap dooda diwap diwap diwap"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """rock bap dooda diwap diwap diwap"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
