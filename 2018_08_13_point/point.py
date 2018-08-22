"""Revised solution to point exercise

Removes _do_binary_op, which was needlessly confusing

08/313/2018
"""


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return (attr for attr in (self.x, self.y, self.z))

    def __repr__(self):
        return "Point({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return (x1, y1, z1) == (x2, y2, z2)

    def __add__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        return Point(*(scalar * coord for coord in self))

    __rmul__ = __mul__  # 2 * Point(x,y,z) == Point(x,y,z) * 2
