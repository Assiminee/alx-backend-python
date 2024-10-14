#!/usr/bin/env python3
"""
Regular function returning asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Calls wait_random and returns it as a created task
    :param max_delay: max delay to wait before returning
    :return: a Task
    """
    return asyncio.create_task(wait_random(max_delay))
