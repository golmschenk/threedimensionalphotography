"""
Tests for the Point class.
"""

from ..point import Point
import numpy as np


class TestPoint:
    """
    Class of tests for Point.
    """

    def test_creation(self):
        """
        Test that a point can be created.
        """
        point = Point()

        assert type(point) is Point

    def test_default_position(self):
        """Test the default position."""
        point = Point()

        assert np.array_equal(point.coordinates, np.array([0, 0, 0]))

    def test_coordinate_setting_on_creation(self):
        """Test coordinates can be passed in during creation."""
        point = Point(1, 2, 3)

        assert np.array_equal(point.coordinates, np.array([1, 2, 3]))

    def test_coordinates_as_settable_computed_attributes(self):
        """Test the coordinates can be set using x, y, and z dot notation."""
        point = Point()

        point.x = 1
        point.y = 2
        point.z = 3

        assert np.array_equal(point.coordinates, np.array([1, 2, 3]))