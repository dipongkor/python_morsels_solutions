from itertools import zip_longest


def add(*matrices):
    """Adds any number of 2D matrices. If
    matrices are not of the same size, raises
    ValueError
    """
    try:
        return [
            [sum(addends) for addends in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError:
        # Raised when sum() is when an addend is None, i.e.,
        # because matrices are different sizes and zip_longest
        # has padded with None
        raise ValueError("Matrices are different sizes")
