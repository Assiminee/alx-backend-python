#!/usr/bin/env python3
"""
Uses an asynchronous coroutine n times, stores the delays
of each coroutine in a list and returns it
"""
import asyncio
from asyncio import as_completed

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    performs n calls of the wait_random method,
    stores the return value of each call in a list,
    returns it.
    :param n: number of calls
    :param max_delay: maximum delay of async coroutine
    :return: list of delays
    """
    tasks: list[asyncio.Task] = [asyncio.create_task(wait_random(max_delay))
                                 for _ in range(n)]
    delays: list = []
    for task in as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    return delays
