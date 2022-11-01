from datacube_ows.band_utils import scalable


def invert_alpha(data):
    return -255 * data["s2cloudless_prob"] + 255


@scalable
def black_cloud(data, band, band_mapper=None):
    cloudless_prob = 1.0 - data["s2cloudless_prob"]
    if band_mapper:
        band = band_mapper(band)
    return data[band] * cloudless_prob
