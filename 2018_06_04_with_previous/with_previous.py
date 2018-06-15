def with_previous(sequence, **kwargs):
    """Passes all bonuses"""
    prev = kwargs.get("fillvalue")  # Defaults to None
    for item in sequence:
        yield (item, prev)
        prev = item
