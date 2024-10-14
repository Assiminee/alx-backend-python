#!/usr/bin/python3
"""
Defines an asynchronous coroutine
that performs a task
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and returns
    the number of seconds awaited
    :return:
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
