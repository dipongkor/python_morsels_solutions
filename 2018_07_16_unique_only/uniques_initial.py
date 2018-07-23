"""Initial solution to Uniques Only exercise

07/16/2018
"""
from collections import Counter


def uniques_only(iterable):
    """Given an iterable, return an iterator containing all of
    the elements in the initial iterable except for duplicates

    - Returns an iterator
    - Works with unhashable objects
    """
    try:
        # This will raise TypeError if elements in iterable are unhashable
        uniques = Counter(iterable)
    except TypeError:
        uniques = []
        for item in iterable:
            dupe_found = False
            for element in uniques:
                if item == element:
                    dupe_found = True
                    break
            if not dupe_found:
                uniques.append(item)
    return (key for key in uniques)
