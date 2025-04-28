#!/usr/bin/env python3
import asyncio
import random
from typing import AsyncGenerator
"""Module that contains an asynchronous generator"""


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that yields a random number between 0 and 10.
    The coroutine will loop 10 times, and wait 1 second each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
