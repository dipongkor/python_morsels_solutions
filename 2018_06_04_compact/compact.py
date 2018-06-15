def compact(sequence):
    """Passes 1st bonus (accept iterator) and
    2nd bonus (return generator)
    """
    for item in sequence:
        try:
            if item != last:
                yield item
                last = item
        except NameError:
            yield item
            last = item
