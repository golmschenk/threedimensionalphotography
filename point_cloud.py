"""
Point cloud stuff.
"""
from random import choice
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
        self.ptx_size = None

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
        centered_self = self.attain_centered_point_cloud()
        centered_other = point_cloud.attain_centered_point_cloud()
        H = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        for i in range(len(centered_self.points)):
            q0 = centered_self.points[i]
            q1 = centered_other.points[i]
            H = np.add(H,
                       np.array([[np.dot(q1.x, q0.x), np.dot(q1.x, q0.y), np.dot(q1.x, q0.z)],
                                 [np.dot(q1.y, q0.x), np.dot(q1.y, q0.y), np.dot(q1.y, q0.z)],
                                 [np.dot(q1.z, q0.x), np.dot(q1.z, q0.y), np.dot(q1.z, q0.z)]]))
        U, _, V = np.linalg.svd(H)
        R = np.dot(V.T, U.T).T # If there's a problem somewhere, it's here.
        p0 = self.attain_centroid()
        p1 = point_cloud.attain_centroid()
        T = np.array([np.subtract(p1.coordinates, np.dot(R, p0.coordinates))])
        padding = np.array([[0, 0, 0, 1]])
        transformation_matrix = np.concatenate((np.concatenate((R, T.T), 1), padding))
        return transformation_matrix

    def attain_correspondences_to_cloud(self, cloud, threshold):
        correspondences = []
        i = 0
        while i < len(self.points):
            point = self.points[i]
            correspondence = point.attain_closest_point_in_cloud(cloud)
            if correspondence.attain_distance_to_point(point) < threshold:
                correspondences.append(correspondence)
                i += 1
            else:
                self.points.pop(i)

        return PointCloud(*correspondences)

    def random_sample(self, size):
        sample = PointCloud()
        for _ in range(size):
            sample.points.append(choice(self.points))
        return sample

    def icp_iteration(self, other, sample_size=100, threshold=2.0):
        sample = self.random_sample(sample_size)
        correspondences = sample.attain_correspondences_to_cloud(other, threshold)
        transformation = sample.attain_transformation_to_point_cloud(correspondences)
        self.transform(transformation)
