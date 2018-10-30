import datetime

from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    """For a given month and year, get a datetime.date object
    for the nth given day of the week in that month
    """
    day = datetime.date(year=year, month=month, day=1)  # First day of month
    month = day.month
    cur_n = 0
    while True:
        if day.weekday() == weekday:
            cur_n += 1
            break
        day = day + datetime.timedelta(days=1)
    while True:
        if day.month != month:
            # We're no longer in the target month because nth is too large
            raise ValueError("nth is too large for target month and weekday")
        if cur_n == nth:
            return day
        day = day + datetime.timedelta(weeks=1)
        cur_n += 1
    return day
