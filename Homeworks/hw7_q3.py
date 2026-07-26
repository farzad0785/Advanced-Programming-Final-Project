#Name: Aliasghar Rashidabadi
#Course: Advanced Programming
#Student ID: 40419533

import math

class Circle(object):
    def __init__(self, radius):
        # initializes self with radius
        self.r = radius

    def get_radius(self):
        # returns radius of self
        return self.r

    def set_radius(self, radius):
        # changes the radius attribute of self to radius
        self.r = radius

    def area(self):
        # computes and returns area of self
        return math.pi * (self.r**2)

    def __eq__(self, other):
        # other is a Circle object
        # returns True if self and other has the same radius value
        return self.r == other.r

    def __gt__(self, other):
        # other is a Circle object
        # returns self or other, Circle object with the bigger radius
        if self.r > other.r:
            return self
        elif self.r < other.r:
            return other

        #otherwise their equal
        return None

    def __add__(self, other):
        # other is a Circle object
        # returns a new Circle object that it's radius is
        #  the sum of self and other's radius
        new_r = self.r + other.r
        return new_r

    def __str__(self):
        # a Circle's string representation is the radius
        return f"Circle radius: {self.r}"

