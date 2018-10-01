class minmax_val(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        yield self.min
        yield self.max


def minmax(items, key=lambda x: x):
    min, max = None, None
    for item in items:
        if min is None or key(min) > key(item):
            min = item
        if max is None or key(max) < key(item):
            max = item
    if min is None or max is None:
        # Iterable was empty
        raise ValueError()
    return minmax_val(min, max)
