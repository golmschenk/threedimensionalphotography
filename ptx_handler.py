"""
PTX file reader and writer.
"""
from point import Point
from point_cloud import PointCloud


class PtxHandler:
    """
    Class for handling PTX files.
    """
    def point_cloud_from_ptx(self, filename):
        """
        Generates a point cloud from a PTX file.
        :param filename: string
        :return: PointCloud
        """
        with open(filename) as file:
            lines = file.readlines()
            points = []
            for line in lines[10:]:
                x, y, z, _ = map(float, line.split(' '))
                points.append(Point(x, y, z))
            return PointCloud(points)

    def ptx_from_point_cloud(self, filename, point_cloud):
        """
        Generates a PTX file from a point cloud.
        :param filename: string
        :return:
        """
        with open(filename, 'w') as file:
            file.write("1\n1\n0 0 0\n1 0 0\n0 1 0\n0 0 1\n1 0 0 0\n0 1 0 0\n0 0 1 0\n0 0 0 1\n")
            for point in point_cloud.points:
                file.write("%f %f %f 1\n" % (point.x, point.y, point.z))


