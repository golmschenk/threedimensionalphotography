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
        self.coordinates[0] = arg

    x = property(None, set_x)

    def set_y(self, arg):
        self.coordinates[1] = arg

    y = property(None, set_y)

    def set_z(self, arg):
        self.coordinates[2] = arg

    z = property(None, set_z)
