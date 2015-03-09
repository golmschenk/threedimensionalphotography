"""
PTX file reader and writer.
"""
from point import Point
from point_cloud import PointCloud


class PtxHandler:
    """
    Class for handling PTX files.
    """
    @classmethod
    def point_cloud_from_ptx(cls, filename):
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
            point_cloud = PointCloud(*points)
            point_cloud.ptx_size = (int(lines[0]), int(lines[1]))

    @classmethod
    def ptx_from_point_cloud(cls, filename, point_cloud):
        """
        Generates a PTX file from a point cloud.
        :param filename: string
        :return:
        """
        with open(filename, 'w') as file:
            if point_cloud.ptx_size:
                s0 = point_cloud.ptx_size[0]
                s1 = point_cloud.ptx_size[1]
            else:
                s0 = len(point_cloud.points)
                s1 = 1
            file.write("%d\n%d\n0 0 0\n1 0 0\n0 1 0\n0 0 1\n1 0 0 0\n0 1 0 0\n0 0 1 0\n0 0 0 1\n" % (s0, s1))
            for point in point_cloud.points:
                file.write("%f %f %f 1\n" % (point.x, point.y, point.z))


