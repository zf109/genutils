"""
    collection of type operations
"""

import numpy as np

def normal(x):
    """
        If x is of customised datatype (from numpy or other), then convert it to normal in-built type 
        otherwise keep as it is

        Args:
        --------
            x: a python object

        Returns:
        --------
            x normalised
    """
    normal_x = int(x) if (isinstance(x, np.int64) or isinstance(x, np.bool_)) else x
    normal_x = float(x) if isinstance(x, np.float64) else x
    return normal_x

