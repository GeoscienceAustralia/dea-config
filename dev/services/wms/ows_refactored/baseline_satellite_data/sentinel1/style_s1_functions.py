import numpy as np
from datacube_ows.band_utils import scalable


@scalable
def db(data, band):
    """Converts Linear intensity values to dB."""
    band_db = 10 * np.log10(data[band])
    band_db = band_db.where(np.isfinite(band_db))
    return band_db


@scalable
def db_difference(data, band1, band2):
    """Returns the difference between two bands in dB."""
    db_band1 = db(data, band1)
    db_band2 = db(data, band2)
    db_difference = db_band1 - db_band2
    return db_difference.where(np.isfinite(db_difference))


def sar_ice_overlay(data, band1, band2, min_val, max_val, gamma=1.0):
    """
    Overlay the bands for 2 bands for SAR-Ice.
    """
    top = np.sqrt(data[band1] + 0.002)
    bottom = np.sqrt(data[band2] + 0.002)
    overlay = ((1 - 2 * top) * bottom + 2 * top) * bottom
    band_data = np.clip(overlay, min_val, max_val)
    normalised = (band_data - min_val) / (max_val - min_val)
    return 255 * (normalised ** (1/gamma))


def sar_ice_square_root_stretch(data, band, min_val, max_val, gamma=1.0):
    """
    Square root and stretch a single band for SAR-Ice.
    """
    band_data = data[band]
    band_data = np.sqrt(band_data + 0.002)
    band_data = np.clip(band_data, min_val, max_val)
    normalised = (band_data - min_val) / (max_val - min_val)
    return 255 * (normalised ** (1/gamma))
