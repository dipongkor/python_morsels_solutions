"""Python Morsels Exercise: get_earliest

First attempt - 2018-05-22
"""


def get_earliest(*args):
    earliest = None
    for date in args:
        split_date = date.split("/")
        month = split_date[0]
        day = split_date[1]
        year = split_date[2]
        value = int(year + month + day)
        if earliest is None:
            earliest = (date, value)
        elif value < earliest[1]:
            earliest = (date, value)
    return earliest[0]


# def get_earliest_old(*args):
#     # Take each "MM/DD/YYYY" arg and convert it to a
#     # int YYYYMMDD
#     dates = {}
#     for arg in args:
#         split_date = arg.split("/")
#         month = split_date[0]
#         day = split_date[1]
#         year = split_date[2]
#         dates[arg] = int(year + month + day)
#     # Find the earliest date (i.e., the smallest int)
#     earliest = None
#     for date, value in dates.items():
#         if earliest is None:
#             earliest = (date, value)
#         elif value < earliest[1]:
#             earliest = (date, value)
#     return earliest[0]
