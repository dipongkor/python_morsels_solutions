"""Revised solution to lstrip exercise (using dropwhile())

08/06/2018
"""

import itertools


def lstrip(iterable, to_skip):
    """Given an iterable, return a generator that
    yields all elements in the original iterable
    except those at the beginning of the iterable
    that match the to_skip argument

    to_skip can alternatively be a function called
    on each item in the original iterable - if its
    return value is truthy, the item is skipped if
    at the beginning of the list
    """
    if callable(to_skip):
        predicate = to_skip
    else:
        def predicate(item):
            return item == to_skip
    return itertools.dropwhile(predicate, iterable)
