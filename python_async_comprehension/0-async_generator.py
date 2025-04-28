#!/usr/bin/env python3
"""Async Comprehension module blabla blabl blabla blabl blabl"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Async Comprehension module blabla blabl blabla blabl blabl"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
