"""
Tests for the PointCloud class.
"""

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