"""Initial solutions to circle exercise

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
        return "Circle({})".format(self._radius)

    def set_radius(self, new_rad):
        if new_rad < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = new_rad

    def get_radius(self):
        return self._radius

    def set_diameter(self, new_dia):
        self.radius = new_dia / 2

    def get_diameter(self):
        return self.radius * 2

    def set_area(self, new_area):
        raise AttributeError("Area cannot be set directy")

    def get_area(self):
        return pi * self.radius ** 2

    radius = property(get_radius, set_radius)
    diameter = property(get_diameter, set_diameter)
    area = property(get_area, set_area)
