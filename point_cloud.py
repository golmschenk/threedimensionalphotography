"""
Point cloud stuff.
"""
import numpy as np

from point import Point

class PointCloud:
    """
    Class for the point cloud.
    """

    def __init__(self, *args):
        """:type : list of [Point]"""
        if not args:
            self.points = []
        else:
            self.points = args

    def __eq__(self, other):
        return all(point == other.points[i] for i, point in enumerate(self.points))

    def transform(self, transformation_matrix):
        """
        Preforms a tranformation on the entire cloud.
        :param transformation_matrix: np.ndarray
        :return:
        """
        for point in self.points:
            point.transform(transformation_matrix)

    def attain_global_rotation(self):
        p0 = self.points[0].coordinates
        p1 = self.points[1].coordinates
        p2 = self.points[2].coordinates

        x = Point(a=np.divide(np.subtract(p0, p1), Point(a=p0).attain_distance_to_point(Point(a=p1))))
        y_non_unit = Point(a=np.subtract(np.subtract(p2, p0), np.dot(np.dot(np.subtract(p2, p0), x.coordinates), x.coordinates)))
        y = Point(a=y_non_unit.coordinates / y_non_unit.attain_vector_length())
        z = Point(a=np.cross(x.coordinates, y.coordinates))

        return np.concatenate((x.coordinates, y.coordinates, z.coordinates), 1).reshape(3, 3).transpose()

    def attain_exact_transformation_to_point_cloud(self, point_cloud):
        """
        Finds the transformation to another point cloud.
        :param point_cloud: PointCloud
        :return transformation_matrix: np.ndarray
        """
        rotation_self = self.attain_global_rotation()
        rotation_other = point_cloud.attain_global_rotation()
        rotation = np.dot(rotation_other, rotation_self.transpose())

        translation = np.array([np.subtract(point_cloud.points[0].coordinates, np.dot(rotation, self.points[0].coordinates))])
        padding = np.array([[0, 0, 0, 1]])
        transformation = np.concatenate((np.concatenate((rotation, translation.T), 1), padding))
        return transformation

    def attain_centroid(self):
        """
        Gets the centroid of a point cloud.
        :return centroid: Point
        """
        sum = np.array([0, 0, 0])
        for point in self.points:
            sum = np.add(sum, point.coordinates)
        return Point(a=np.divide(sum, len(self.points)))

    def attain_centered_point_cloud(self):
        """
        Gets the point cloud centered around the centroid as the origin.
        :return centered_point_cloud: PointCloud
        """
        centered_point_cloud = PointCloud()
        centroid = self.attain_centroid()
        for point in self.points:
            centered_point_cloud.points.append(Point(a=np.subtract(point.coordinates, centroid.coordinates)))
        return centered_point_cloud

    def attain_transformation_to_point_cloud(self, point_cloud):
        """
        Finds the exact transformation to another point cloud.
        :param point_cloud: PointCloud
        :return transformation_matrix: np.ndarray
        """
        pass



