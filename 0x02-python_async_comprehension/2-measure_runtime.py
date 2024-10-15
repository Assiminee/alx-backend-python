#!/usr/bin/env python3
"""
Measures runtime and returns it
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times in parallel using
    :return: the total runtime
    """
    start = time()
    awaitables = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*awaitables)
    end = time()
    return end - start
