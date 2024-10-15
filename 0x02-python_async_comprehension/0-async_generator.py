#!/usr/bin/env python3
"""
Contains an async generator function
"""
import asyncio
import random
from typing import Generator, List


async def generate() -> Generator[int, any, any]:
    """
    coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10
    :return:
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 5)


async def async_generator() -> List[int]:
    """
    returns a list of random numbers using list comprehension
    in asynchronous methods
    :return:
    """
    return [i async for i in generate()]
