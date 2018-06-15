def with_previous(sequence, **kwargs):
    """Passes 1st and 3rd bonuses, fails 2nd bonus"""
    prev = kwargs.get("fillvalue")  # Defaults to None
    tups = []
    for item in sequence:
        tups.append((item, prev))
        prev = item
    return tups
