"""Initial solution to interleave exercise

08/27/2018
"""

from itertools import chain


def interleave(iterable1, iterable2):
    """Interleave the elements of two iterables and return an iterator"""
    return chain.from_iterable(zip(iterable1, iterable2))
