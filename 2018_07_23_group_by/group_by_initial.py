"""Initial solution to Group By exercise

07/23/2018
"""


def group_by(iterable, key_func=lambda x: x):
    """Given an iterable, return a dict-like object
    where elements in the iterable are grouped
    according to their value when passed to key_func

    - When no key_func is passed, key_func is identity
    """
    groups = {}
    for item in iterable:
        try:
            groups[key_func(item)].append(item)
        except KeyError:
            groups[key_func(item)] = [item]
    return groups
