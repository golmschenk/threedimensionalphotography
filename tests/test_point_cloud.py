"""
Tests for the PointCloud class.
"""
from unittest import mock
from unittest.mock import MagicMock
import numpy as np
from math import cos, sin
from mathematics import π

from ..point_cloud import PointCloud
from ..point import Point


class TestPointCloud:
    """
    Class of tests for PointCloud.
    """
    def test_creation(self):
        """
        Test that a point cloud can be created.
        """
        point_cloud = PointCloud()

        assert type(point_cloud) is PointCloud

    def test_setting_points_on_creation(self):
        """Test coordinates can be passed in during creation."""
        point0 = Point(1, 2, 3)
        point1 = Point(4, 5, 6)
        point_cloud = PointCloud(point0, point1)

        assert point0 in point_cloud.points
        assert point1 in point_cloud.points

    def test_transformation(self):
        """Test tranformation."""
        def mock_transform(self, _):
            if self == Point(1, 2, 3):
                self.coordinates = np.array([3, 0, 6])
            elif self == Point(4, 5, 6):
                self.coordinates = np.array([6, -3, 9])
        with mock.patch.object(Point, "transform", autospec=True) as transform:
            transform.side_effect = mock_transform

            point_cloud = PointCloud(Point(1, 2, 3), Point(4, 5, 6))
            transformation = np.array([[1, 0,        0,         2],
                                       [0, cos(π/2), -sin(π/2), 3],
                                       [0, sin(π/2),  cos(π/2), 4],
                                       [0, 0,        0,         1]])

            point_cloud.transform(transformation)

            assert Point(3, 0, 6) in point_cloud.points
            assert Point(6, -3, 9) in point_cloud.points
