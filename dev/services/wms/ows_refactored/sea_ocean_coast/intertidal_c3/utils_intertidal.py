from datacube_ows.band_utils import scalable


@scalable
def elevation_adaptive(data, band, lot, hot, band_mapper=None):
    """
    Experimental adaptive elevation function, using pixel-level
    tide metadata to calculate relative elevation for any
    given location.

    This implementation should be free of any tile-based
    discontinuities in the resulting visualisation.

    # TODO: Add hillshading
    """

    # Calculate observed tide range (max - min)
    otr = data[hot] - data[lot]

    # Calculate distance between elevation and minumum
    # observed tide height
    distance_to_min = data[band] - data[lot]

    # Calculate proportion along observed tide range
    proportion_array = distance_to_min / otr

    return proportion_array


@scalable
def uncertainty_adaptive(data, band, lot, hot, band_mapper=None):
    """
    Experimental adaptive elevation uncertainty function, using
    pixel-level tide metadata to calculate relative uncertainty.
    """

    # Calculate observed tide range (max - min)
    otr = data[hot] - data[lot]

    # Calculate proportion
    proportion_array = data[band] / otr

    return proportion_array


def multi_date_raw_elevation(data, band, band_mapper=None):
    """
    Compares two elevation layers and calculates difference in elevation.
    """
    data1, data2 = (data.sel(time=dt) for dt in data.coords["time"].values)

    return data2[band] - data1[band]
