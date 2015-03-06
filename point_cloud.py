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
