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
    if band_mapper is not None:
        band = band_mapper(band)

    data1, data2 = (data.sel(time=dt) for dt in data.coords["time"].values)

    return data2[band] - data1[band]


def tide_graph_path(data, ds):
    """
    Calculates an additional metadata field providing the
    URL to a graph used to visualise tide biases.
    """

    # Extract required data from datacube dataset
    base_dir = "https://dea-public-data.s3-ap-southeast-2.amazonaws.com/derivative"
    product = ds.metadata_doc['properties']['odc:product']
    version = ds.metadata_doc['properties']['odc:dataset_version'].replace(".", "-")
    year = ds.metadata_doc['properties']['datetime'][:4]
    region = ds.metadata_doc['properties']['odc:region_code']
    region_split = region.replace("y", "/y")

    # Combine into a string
    return f"{base_dir}/{product}/{version}/{region_split}/{year}--P1Y/{product}_{region}_{year}--P1Y_final_tide_graph.png"
