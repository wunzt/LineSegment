# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/22/2022
# Description: Uses two classes to represent points and lines on a graph, giving length, slope, and parallel values to lines.

class Point:
    """Takes two coordinates and returns them as a point. Returns the distance between two given points."""

    def __init__(self, x_coord, y_coord):
        """Initializes the x and y coordinates."""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """Returns the x coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Returns the y coordinate."""
        return self._y_coord

    def distance_to(self, target):
        """Returns the distance between two points."""
        return abs(((target.get_x_coord() - self.get_x_coord())**2 + (target.get_x_coord() - self.get_y_coord())**2)**0.5)



class LineSegment:
    """Takes two points and returns the length, slope, and parallel values of the resulting line segment."""

    def __init__(self, Point_1, Point_2):
        """Initializes the points of the line segment."""
        self._Point_1 = Point_1
        self._Point_2 = Point_2

    def get_endpoint_1(self):
        """Returns endpoint 1."""
        return self._Point_1

    def get_endpoint_2(self):
        """Returns endpoint 2."""
        return self._Point_2

    def length(self):
        """Returns the length of the line segment."""
        return self.get_endpoint_1().distance_to(self.get_endpoint_2())

    def is_parallel_to(self, segment_2):
        """Returns whether or not two line segments are parallel as a Boolean."""
        return self.slope() == segment_2.slope()

    def slope(self):
        """Returns the slope of the line segment."""
        rise = self.get_endpoint_2().get_y_coord() - self.get_endpoint_1().get_y_coord()
        run = self.get_endpoint_2().get_x_coord() - self.get_endpoint_1().get_x_coord()
        return rise/run #There are issues with run equal to 0 that would need to be addressed for more complete code.