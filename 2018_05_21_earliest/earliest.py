def get_earliest(*dates):
    earliest_tup, earliest_str = None, None
    for date in dates:
        month, day, year = date.split("/")
        if earliest_tup is None or earliest_tup > (year, month, day):
            earliest_tup, earliest_str = (year, month, day), date
    return earliest_str
