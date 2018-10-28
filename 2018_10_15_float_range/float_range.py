from math import ceil


def _attributes(self):
    if len(self) == 0:
        return ()
    step = 1 if len(self) == 1 else self.step
    return (next(iter(self)), next(reversed(self)), step)


class float_range(object):
    def __init__(self, *args):
        if not args:
            raise TypeError("Must provide at least stop argument")
        elif len(args) == 1:
            self.start, self.stop, self.step = 0.0, args[0], 1.0
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1.0
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
        else:
            raise TypeError("float_range() takes maximum 3 args")

        if self.step == 0.0:
            raise ValueError("Step must not be 0.0")

    def __iter__(self):
        cur = self.start
        for _ in range(len(self)):
            yield cur
            cur += self.step

    def __reversed__(self):
        cur = self.start + (len(self)-1) * self.step
        for _ in range(len(self)):
            yield cur
            cur -= self.step

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return _attributes(self) == _attributes(other)
        else:
            return NotImplemented

    def __len__(self):
        length = ceil((self.stop - self.start) / self.step)
        return length if length > 0 else 0
