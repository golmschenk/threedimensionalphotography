"""
Point cloud stuff.
"""

class PointCloud:
    """
    Class for the point cloud.
    """

    def __init__(self, *args):
        """:type : list of [Point]"""
        self.points = args

    def transform(self, transformation_matrix):
        """
        Preforms a tranformation on the entire cloud.
        :param transformation_matrix: np.ndarray
        :return:
        """
        for point in self.points:
            point.transform(transformation_matrix)

    def attain_transformation_to_point_cloud(self, point_cloud):
        """
        Finds the transfomation to another point cloud.
        :param point_cloud: PointCloud
        :return transformation_matrix: np.ndarray
        """
        p0 = self.points[0]
        p1 = self.points[1]
        p2 = self.points[2]

