"""
Tests for the Point class.
"""

from ..point import Point
from mathematics import π, almost_equal

import numpy as np
from math import cos, sin
from point_cloud import PointCloud


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

    def test_coordinates_as_gettable_computed_attributes(self):
        """Test the ability to get coordinates using x, y, and z dot notation."""
        point = Point(1, 2, 3)

        assert point.x == 1
        assert point.y == 2
        assert point.z == 3

    def test_x_axis_rotation(self):
        """Test rotation on the x-axis."""
        point = Point(1, 1, 1)
        rotation = np.array([[1, 0, 0], [0, cos(π/2), -sin(π/2)], [0, sin(π/2), cos(π/2)]])

        point.rotate(rotation)

        assert almost_equal(point.x, 1)
        assert almost_equal(point.y, -1)
        assert almost_equal(point.z, 1)

    def test_z_axis_rotation(self):
        """Test rotation on the x-axis."""
        point = Point(1, 1, 1)
        rotation = np.array([[cos(π/2), -sin(π/2), 0], [sin(π/2), cos(π/2), 0], [0, 0, 1]])

        point.rotate(rotation)

        assert almost_equal(point.x, -1)
        assert almost_equal(point.y, 1)
        assert almost_equal(point.z, 1)

    def test_y_axis_rotation(self):
        """Test rotation on the x-axis."""
        point = Point(1, 1, 1)
        rotation = np.array([[cos(π/2), 0, sin(π/2)], [0, 1, 0], [-sin(π/2), 0, cos(π/2)]])

        point.rotate(rotation)

        assert almost_equal(point.x, 1)
        assert almost_equal(point.y, 1)
        assert almost_equal(point.z, -1)

    def test_translation(self):
        point = Point(1, 1, 1)
        translation = np.array([2, 3, 4])

        point.translate(translation)

        assert almost_equal(point.x, 3)
        assert almost_equal(point.y, 4)
        assert almost_equal(point.z, 5)

    def test_transformation(self):
        point = Point(1, 1, 1)
        transformation = np.array([[1, 0, 0, 2], [0, cos(π/2), -sin(π/2), 3], [0, sin(π/2), cos(π/2), 4], [0, 0, 0, 1]])

        point.transform(transformation)

        assert almost_equal(point.x, 3)
        assert almost_equal(point.y, 2)
        assert almost_equal(point.z, 5)

    def test_transformation2(self):
        point = Point(1, 2, 3)
        transformation = np.array([[1, 0, 0, 2], [0, cos(π/2), -sin(π/2), 3], [0, sin(π/2), cos(π/2), 4], [0, 0, 0, 1]])

        point.transform(transformation)

        assert almost_equal(point.x, 3)
        assert almost_equal(point.y, 0)
        assert almost_equal(point.z, 6)

    def test_distance_to_another_point(self):
        point0 = Point(1, 1, 1)
        point1 = Point(2, 2, 2)
        point2 = Point(3, 3, 3)

        distance0 = point0.attain_distance_to_point(point1)
        distance1 = point0.attain_distance_to_point(point2)

        assert distance0 == 3**(1/2.0)
        assert distance1 == 12**(1/2.0)

    def test_find_vector_length(self):
        point = Point(2, 2, 2)

        length = point.attain_vector_length()

        assert length == 12**(1/2.0)

    def test_finding_closest_point_in_cloud(self):
        point_cloud = PointCloud(Point(1, 1, 1), Point(1, 3, 1), Point(3, 1, 1), Point(3, 3, 1))
        expected_closet_point = Point(1, 1, 1)
        point = Point(-1, -1, -1)

        closest_point = point.attain_closest_point_in_cloud(point_cloud)

        assert closest_point == expected_closet_point
