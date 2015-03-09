"""
File for running random scripts.
"""
import numpy as np
from math import cos, sin

from mathematics import π
from point_cloud import PointCloud
from point import Point
from ptx_handler import PtxHandler
from pcl_interface import PclInterface

point_cloud0 = PtxHandler.point_cloud_from_ptx("ptx/gh17to16close.ptx")
point_cloud1 = PtxHandler.point_cloud_from_ptx("ptx/gh16.ptx")
point_cloud0.icp_iteration(point_cloud1, 1000, 0.1)
#transformation, point_cloud2 = PclInterface.icp(point_cloud0, point_cloud1)
PtxHandler.ptx_from_point_cloud("ptx/test.ptx", point_cloud0)
print('End')
