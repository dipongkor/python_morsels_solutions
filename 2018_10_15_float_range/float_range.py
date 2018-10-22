def float_range(*args):
    if not args:
        raise TypeError("Must provide stop argument")
    elif len(args) == 1:
        start, stop, step = 0.0, args[0], 1.0
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1.0
    elif len(args) == 3:
        start, stop, step = args[0], args[1], args[2]
    else:
        raise TypeError("float_range() takes maximum 3 args")

    if step == 0.0:
        raise ValueError("Step must not be 0.0")

    def float_range_inner(start, stop, step):
        def should_continue():
            if step > 0:
                return cur < stop
            else:
                return cur > stop
        cur = start
        while should_continue():
            print("Value of cur: {}".format(cur))
            yield cur
            cur += step

    return float_range_inner(start, stop, step)
