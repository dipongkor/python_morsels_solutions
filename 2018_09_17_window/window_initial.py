from collections import deque


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
    q = deque()
    it = iter(iterable)
    while True:
        try:
            q.append(next(it))
            if len(q) == n:
                yield tuple(q)
                q.popleft()
        except StopIteration:
            break
