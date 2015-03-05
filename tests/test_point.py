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
        point = Point()

        assert type(point) is Point

    def test_default_position(self):
        point = Point()

        assert np.array_equal(point.coordinates, np.array([0, 0, 0]))