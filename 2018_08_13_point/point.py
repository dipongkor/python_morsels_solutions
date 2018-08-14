"""Initial solution to point exercise

08/313/2018
"""


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return (attr for attr in (self.x, self.y, self.z))

    def __str__(self):
        return "Point({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def _do_binary_op(self, other, op):
        return Point(*[op(a, b) for a, b in zip(self, other)])

    def __add__(self, other):
        return self._do_binary_op(other, op=lambda x, y: x + y)

    def __sub__(self, other):
        return self._do_binary_op(other, op=lambda x, y: x - y)

    def __mul__(self, factor):
        other = Point(factor, factor, factor)
        return self._do_binary_op(other, op=lambda x, y: x * y)

    __rmul__ = __mul__  # 2 * Point(x,y,z) == Point(x,y,z) * 2
