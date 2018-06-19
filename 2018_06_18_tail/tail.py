"""First attempt - 6/18/18"""


def tail(iterable, n):
    """Given an iterable, returns a list containing
    the last n elements in the iterable
    """
    tail_elements = []
    if n > 0:
        for element in iterable:
            tail_elements.append(element)
            if len(tail_elements) > n:
                # tail_elements is past max length, and we need
                # to remove the first element
                tail_elements = tail_elements[-n:]
    return tail_elements
