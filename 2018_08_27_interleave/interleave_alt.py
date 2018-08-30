"""Alternate solution to interleave exercise

08/30/2018
"""


def interleave(iterable1, iterable2):
    """Interleave the elements of two iterables and return an iterator"""
    for x, y in zip(iterable1, iterable2):
        yield x
        yield y
