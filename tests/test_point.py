"""
Tests for the Point class.
"""

from ..point import Point


class TestPoint:
    """
    Class of tests for Point.
    """

    def test_creation(self):
        point = Point()

        assert type(point) is Point
        