"""Revised attempt - 6/22/18"""
from collections import deque


def tail(iterable, n):
    """Given an iterable, returns a list containing
    the last n elements in the iterable
    """
    if n < 1:
        return []
    return list(deque(iterable, maxlen=n))
