"""
Implement a simple Point class. A point is represented by a pair of x,y cartesian coordinates.
"""
import math


class Point:
    """
    Class to make an instance of a Cartesian point
    """

    def __init__(self, x=0, y=0):
        """
        Initializes values for the x & y coordinates

        :param x:
        :param y:

        Note the use of single and double underscores in the instance variables.
        This INDICATES privacy although the concept is not enforced in Python. The double underscores implement
        'name mangling'. This makes deriving the actual name slightly more complicated but it doesn't really
        fool anybody.
        """
        self._x = x
        self.__y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
        # return "Point({},{})".format(self._x, self.__y)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"
        # return self.__str__()

    def distance(self, other_point):
        """
        Computes the distance between two points based on Pythagoras' theorem.

        :param other_point:
        :return: distance value
        """
        if not isinstance(other_point, self.__class__):
            raise TypeError(f"ERROR: {other_point} is not a valid {self.__class__.__name__} object")
        return math.sqrt(((abs(self._x - other_point._x)) ** 2) + ((abs(self.__y - other_point.__y)) ** 2))

    def __add__(self, other_point):
        if not isinstance(other_point, self.__class__):
            raise TypeError(f"ERROR: {other_point} is not a valid {self.__class__.__name__} object")
        return self.__class__(self.x + other_point.x, self.y + other_point.y)

    @property
    def x(self):
        """
        Return the x coordinate value. Note the @property 'decorator'. This makes the function called 'x' act as a
        property (instance variable) of the object. asking for (e.g.) my_point.x will fire this method. This is like
        a 'getter' method in other languages. It acts as a gatekeeper for the 'private' instance variable.
        """
        return self._x

    @property
    def y(self):
        return self.__y


if __name__ == "__main__":
    try:
        point1 = Point(2, 3)
        point2 = Point(4, 8)
        point3 = point1 + point2
        point4 = point1.__add__(point2)
        int1 = 5

        print(f"{point1}, {point2}, {point3}, {point4}")
        print(f"Distance from {point1} to {point2} is {point1.distance(point2):5.3f}")
        print(f"Distance from {point1} to {int1} is {point1.distance(int1):5.3f}")
    except Exception as e:
        print(f"{e}\nI'm shutting down")
        quit(1)