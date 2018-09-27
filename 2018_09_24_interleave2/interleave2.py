"""
Function that accepts two or more iterables and returns a
new iterator with each of the given items "interleaved"
(item 0 from iterable 1, then item 0 from iterable 2,
then item 1 from iterable 1, etc.)
"""


def interleave(*iterables):
    exhausted = set()
    iterators = [iter(iterable) for iterable in iterables]
    while len(exhausted) < len(iterators):
        for iterator in iterators:
            if iterator not in exhausted:
                try:
                    yield next(iterator)
                except StopIteration:
                    exhausted.add(iterator)
