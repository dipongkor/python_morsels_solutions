def numeric_range(list):
    min = None
    max = None

    for element in list:
        if min is None or min > element:
            min = element
        if max is None or max < element:
            max = element
    if min is None or max is None:
        return 0
    else:
        return max - min
