"""Parse a string representation of several numeric ranges

Returns a generator

>>> nums = parse_ranges('1-3, 8, 18->exit')
>>> next(nums)
1
>>> next(nums)
2
>>> next(nums)
3
>>> next(nums)
8
>>> next(nums)
18
"""


def parse_ranges(range_str):
    ranges_and_numbers = range_str.split(',')
    for item in ranges_and_numbers:
        # Strip out '->' and whatever chars follow it
        item = item.split('->')[0]
        try:
            # item may be a single number, e.g., '25'
            yield int(item)
        except ValueError:
            # Range contained a hypen, e.g., '1-5'
            start, stop = [int(x) for x in item.split('-')]
            for num in range(start, stop + 1):
                yield num
