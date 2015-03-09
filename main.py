"""
File for running random scripts.
"""
import numpy as np
from math import cos, sin

from mathematics import π
from point_cloud import PointCloud
from point import Point
from ptx_handler import PtxHandler

gh17_to_gh23_close = np.array([[0.769006,  0.300208,  0.564362,  15.474807],
                               [-0.340899,  0.939441, -0.035215, -2.941283],
                               [-0.540756, -0.165310,  0.824776, - 4.791782],
                               [0, 0, 0, 1]])

gh17_to_gh16_close = np.array([[0.999953, 0.004953,  0.008324, -0.000003],
                               [-0.003077, 0.977294, -0.211865,  0.001217],
                               [-0.009184, 0.211829,  0.977264,  0.017408],
                               [0, 0, 0, 1]])

point_cloud = PtxHandler.point_cloud_from_ptx("gh17.ptx")
point_cloud.transform(gh17_to_gh23_close)
PtxHandler.ptx_from_point_cloud("gh17to23.ptx", point_cloud)
print('yo')
