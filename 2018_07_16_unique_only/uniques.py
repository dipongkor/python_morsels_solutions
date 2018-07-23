"""Revised solution to Uniques Only exercise

07/23/2018
"""


def uniques_only(iterable):
    """Given an iterable, return an iterator containing all of
    the elements in the initial iterable except for duplicates

    - Returns an iterator
    - Works with unhashable objects
    - Works efficiently with hashable objects (O(1) time to determine if seen)
    """
    hashable = set()
    unhashable = []
    for item in iterable:
        try:
            if item not in hashable:
                # Will raise TypeError if item is unhashable
                yield item
                hashable.add(item)
        except TypeError:
            if item not in unhashable:
                yield item
                unhashable.append(item)
