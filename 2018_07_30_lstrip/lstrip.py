"""Initial solution to lstrip exercise

07/30/2018
"""


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
    unskippable_seen = False
    for item in iterable:
        if unskippable_seen:
            yield item
        else:
            try:
                if not to_skip(item):
                    unskippable_seen = True
                    yield item
            except TypeError:
                if item != to_skip:
                    unskippable_seen = True
                    yield item
