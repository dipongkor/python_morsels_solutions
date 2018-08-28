"""(Terrible) alternate solution to deep_add exercise - gratuitous one-liner

Unreadable and risks RecursionError for large lists

08/21/2018
"""

from collections.abc import Iterable
from functools import reduce


def deep_add(nested_list, start=0):
    return reduce(lambda total, element: total + (deep_add(element) if isinstance(element, Iterable) else element), nested_list, start)
