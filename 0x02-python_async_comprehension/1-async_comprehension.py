#!/usr/bin/env python3
"""
List comprehension using async coroutines
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async
    comprehension over async_generator
    :return: list of random numbers
    """
    return [i async for i in async_generator()]
