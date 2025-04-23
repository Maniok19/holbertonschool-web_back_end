#!/usr/bin/env python3
"""rock bap dooda diwap diwap diwap"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """rock bap dooda diwap diwap diwap"""
    r = asyncio.create_task(wait_random(max_delay))
    return r
