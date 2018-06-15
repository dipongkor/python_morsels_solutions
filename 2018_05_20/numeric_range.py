def numeric_range(iterable):
    # Get first element, if it exists, and
    # initialize min and max to that value
    try:
        iterator = iter(iterable)
        min = max = next(iterator)
    except StopIteration:
        return 0
    for i in iterator:
        if i < min:
            min = i
        if i > max:
            max = i
    return max - min
