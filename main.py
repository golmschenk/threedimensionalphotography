"""
File for running random scripts.
"""
import numpy as np
from math import cos, sin

from mathematics import π
from point_cloud import PointCloud
from point import Point

point_cloud_l = PointCloud(Point(1, 1, 1), Point(1, 5, 4), Point(2, 3, 7), Point(4, 1, 1), Point(4, 5, 4), Point(4, 3, 7))
point_cloud_r = PointCloud(Point(1, 1, 1), Point(1, 5, 4), Point(2, 3, 7), Point(4, 1, 1), Point(4, 5, 4), Point(4, 3, 7))
transformation = np.array([[1, 0,        0,         5],
                           [0, cos(π/4), -sin(π/4), 4],
                           [0, sin(π/4),  cos(π/4), 3],
                           [0, 0,        0,         1]])

point_cloud_l.transform(transformation)
print('yo')
