"""
Stuff to connect my code to the PCL code.
"""
import pcl
import numpy as np
from point import Point
from point_cloud import PointCloud
from pcl.registration import icp as ricp


class PclInterface:
    """
    Class to allow interfacing between threedimensionalphotography and PCL.
    """
    @classmethod
    def point_cloud_to_pcl_point_cloud(cls, point_cloud):
        """
        Convert PointCloud to PCL PointCloud.
        :param point_cloud: PointCloud
        :return: pcl.PointCloud
        """
        return pcl.PointCloud(np.array([c.coordinates for c in point_cloud.points], dtype=np.float32))

    @classmethod
    def pcl_point_cloud_to_point_cloud(cls, pcl_point_cloud):
        """
        Convert PCL PointCloud to PointCloud.
        :param point_cloud: pcl.PointCloud
        :return: PointCloud
        """
        return PointCloud(*[Point(x, y, z) for x, y, z in pcl_point_cloud])

    @classmethod
    def icp(cls, point_cloud0, point_cloud1):
        pcl_point_cloud0 = cls.point_cloud_to_pcl_point_cloud(point_cloud0)
        pcl_point_cloud1 = cls.point_cloud_to_pcl_point_cloud(point_cloud1)
        _, transformation, estimate, _ = ricp(pcl_point_cloud0, pcl_point_cloud1)
        point_cloud_estimate = cls.pcl_point_cloud_to_point_cloud(estimate)
        return transformation, point_cloud_estimate