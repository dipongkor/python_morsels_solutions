"""Initial solution to multimax exercise

07/08/2018
"""


def multimax(iterable, key=lambda x: x):
    """Get a list of the largest elements from an iterable

    - Given an empty iterable, returns an empty list
    - Works with lazy iterables
    - Accepts a keyword argument "key" that is a function
      to be applied to the iterable's elements when comparing
      value

    >>> multimax([1, 2, 3])
    [3]
    >>> multimax([7, 8, 9, 9, 7, 7])
    [9, 9]
    >>> multimax([])
    []
    >>> multimax(i for i in range(10) if i % 2 == 0)
    [8]
    >>> multimax(["cat", "dog", "frog"], key=len)
    ["frog"]
    """

    maxes = []
    largest = None
    for element in iterable:
        if largest is None or key(element) > key(largest):
            maxes = [element]
            largest = element
        elif key(element) == key(largest):
            maxes.append(element)
    return maxes
