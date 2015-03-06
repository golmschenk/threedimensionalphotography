"""
Three dimensional point stuff.
"""

import numpy as np


class Point:
    """
    Three dimensional point class.
    """
    def __init__(self, x=0, y=0, z=0):
        self.coordinates = np.array([x, y, z])

    # Computed attributes
    def set_x(self, arg):
        """
        :param arg: double
        """
        self.coordinates[0] = arg

    def get_x(self):
        """
        Gets the x coordinate.
        """
        return self.coordinates[0]

    x = property(get_x, set_x)

    def set_y(self, arg):
        """
        :param arg: double
        """
        self.coordinates[1] = arg

    def get_y(self):
        """
        Gets the y coordinate.
        """
        return self.coordinates[1]

    y = property(get_y, set_y)

    def set_z(self, arg):
        """
        :param arg: double
        """
        self.coordinates[2] = arg

    def get_z(self):
        """
        Gets the z coordinate.
        """
        return self.coordinates[2]

    z = property(get_z, set_z)

    def rotate(self, rotation_matrix):
        """
        Rotates the point as defined by the rotation matrix.
        :param rotation_matrix: np.ndarray
        """
        self.coordinates = np.dot(rotation_matrix, self.coordinates)