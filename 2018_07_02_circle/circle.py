"""Revised solution to circle exercise using
property/setter decorators

07/03/2018
"""
from math import pi


class Circle():
    """A Circle with attributes radius, diameter, and area

    - Radius should default to 1 if no argument passed to constructor
    - Setting either radius or diameter should update the other attributes
    - Attempting to set area directly should raise an AttributeError
    - Attempting to set radius or diameter to a negative value should
      raise a ValueError
    """

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return "Circle({})".format(self.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_val):
        if new_val < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = new_val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_val):
        self.radius = new_val / 2

    @property
    def area(self):
        return pi * self.radius ** 2
