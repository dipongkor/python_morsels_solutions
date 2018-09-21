"""
Revised solution to window exercise that gets rid of
if statement to check length of queue within body of loop
"""

from collections import deque
from itertools import islice


def window(iterable, n):
    """Return tuples of n consecutive elements in iterable as a generator.

    >>> tups = window([1, 2, 3, 4], 2)
    >>> next(tups)
    (1, 2)
    >>> next(tups)
    (2, 3)
    >>> next(tups)
    (3, 4)
    """
    i = iter(iterable)
    q = deque(islice(i, n), maxlen=n)
    yield tuple(q)
    for item in i:
        q.append(item)
        yield tuple(q)
