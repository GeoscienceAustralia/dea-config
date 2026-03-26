from datacube_ows.band_utils import scalable
from odc.geo.geom import point
from odc.geo.gridspec import GridSpec
from odc.geo.types import xy_


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

    Region codes (e.g. "x123y123") are derived by querying
    the 32km coastal tile grid based on the centroid of
    the dataset returned by the GetFeatureInfo request.
    """
    # Create coastal 32 km gridspec
    gs_sentinel_c3 = GridSpec(
        crs="EPSG:3577",
        resolution=10,
        tile_shape=(3200, 3200),
        origin=xy_(-4416000, -6912000),
    )

    # Get point from GetFeatureInfo data
    y, x = data.y.item(), data.x.item()
    point_albers = point(y=y, x=x, crs="EPSG:3857").to_crs("EPSG:3577").geom
    # point_albers = data.odc.geobox.extent.centroid.to_crs("EPSG:3577").geom

    # Return region code
    tile = gs_sentinel_c3.pt2idx(x=point_albers.x, y=point_albers.y)
    region = f"x{tile.x:03}y{tile.y:03}"
    region_split = region.replace("y", "/y")

    # Extract required data from datacube dataset
    base_dir = "https://dea-public-data.s3-ap-southeast-2.amazonaws.com/derivative"
    product = ds.metadata_doc['properties']['odc:product']
    version = ds.metadata_doc['properties']['odc:dataset_version'].replace(".", "-")
    year = ds.metadata_doc['properties']['datetime'][:4]

    # Combine into a string
    return f"{base_dir}/{product}/{version}/{region_split}/{year}--P1Y/{product}_{region}_{year}--P1Y_final_tide_graph.png"
