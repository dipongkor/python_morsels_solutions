def compact(sequence):
    """Passes 1st bonus (accept iterator) and
    2nd bonus (return generator)
    """
    def generate(seq):
        for item in seq:
            try:
                if item != last:
                    last = item
                    yield item
            except NameError:
                last = item
                yield item
    return generate(sequence)
