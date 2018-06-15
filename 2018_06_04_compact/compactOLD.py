def compact(sequence):
    """Passes 1st bonus (accept iterator), fails
    2nd bonus (return generator)
    """
    no_repeats = []
    for item in sequence:
        try:
            if item != last:
                no_repeats.append(item)
                last = item
        except NameError:
            no_repeats.append(item)
            last = item
    return no_repeats
