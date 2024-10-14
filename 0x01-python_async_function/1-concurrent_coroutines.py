#!/usr/bin/env python3
"""
Uses an asynchronous coroutine n times, stores the delays
of each coroutine in a list and returns it
"""
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
    delays: list = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays
