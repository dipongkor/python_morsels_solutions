def with_previous(sequence, **kwargs):
    """Passes 1st and 3rd bonuses, fails 2nd bonus"""
    def generate(seq, fill):
        last = fill
        for item in seq:
            tmp_last, last = last, item
            yield (item, tmp_last)
    return generate(sequence, kwargs.get("fillvalue"))
