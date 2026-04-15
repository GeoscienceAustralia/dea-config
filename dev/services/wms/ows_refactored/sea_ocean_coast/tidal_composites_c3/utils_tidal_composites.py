import numpy as np
from datacube_ows.band_utils import scalable


@scalable
def log_scaling(data, band):
    """
    Use log scaling to produce a more visually
    attractive three-band image.
    """
    return np.log(data[band] + 1)
