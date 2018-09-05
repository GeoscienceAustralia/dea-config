# Static config for the wms metadata.

from colour import Color
from bisect import bisect
import xarray
import numpy as np
from functools import partial

response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    ## Which web service(s) should be supported by this instance
    "wcs": True,
    "wms": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "WMS server for Australian NBART Datacube products",
    # Service URL.  Should a fully qualified URL
    "url": "https://ows.devkube.services.dea.ga.gov.au",

    # Supported co-ordinate reference systems
    "published_CRSs": {
        "EPSG:3857": {  # Web Mercator
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
        "EPSG:4326": {  # WGS-84
            "geographic": True,
            "vertical_coord_first": True
        },
        "EPSG:3577": {  # GDA-94, internal representation
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
    },

    ## Required config for WCS
    # Must be a geographic CRS in the published_CRSs list.  EPSG:4326 is recommended, but any geographic CRS should work.
    "default_geographic_CRS": "EPSG:4326",

    # Supported WCS formats
    "wcs_formats": {
        # Key is the format name, as used in DescribeCoverage XML
        "GeoTIFF": {
            # Renderer is the FQN of a Python function that takes:
            #   * A WCS Request object
            #   * Some ODC data to be rendered.
            "renderer": "datacube_wms.wcs_utils.get_tiff",
            # The MIME type of the image, as used in the Http Response.
            "mime": "image/geotiff",
            # The file extension to add to the filename.
            "extension": "tif",
            # Whether or not the file format supports multiple time slices.
            "multi-time": False
        },
        "netCDF": {
            "renderer": "datacube_wms.wcs_utils.get_netcdf",
            "mime": "application/x-netcdf",
            "extension": "nc",
            "multi-time": True,
        }
    },
    # The native wcs format must be declared in wcs_formats above.
    "native_wcs_format": "GeoTIFF",

    ## Optional config for instances supporting WMS
    # Max tile height/width.  If not specified, default to 256x256
    "max_width": 512,
    "max_height": 512,

    # Optional config for all services (WMS and/or WCS) - may be set to blank/empty, no defaults
    "abstract": """Historic Landsat imagery for Australia.""",
    "keywords": [
        "geomedian",
        "WOfS",
        "mangrove",
        "landsat",
        "australia",
        "time-series",
    ],
    "contact_info": {
        "person": "Digital Earth Australia",
        "organisation": "Geoscience Australia",
        "position": "",
        "address": {
            "type": "postal",
            "address": "GPO Box 378",
            "city": "Canberra",
            "state": "ACT",
            "postcode": "2609",
            "country": "Australia",
        },
        "telephone": "+61 2 6249 9111",
        "fax": "",
        "email": "earth.observation@ga.gov.au",
    },
    "fees": "",
    "access_constraints": "",
    "preauthenticate_s3": True,
    "geotiff_georeference_source": "INTERNAL"
}

__ramp_values__ = [
    {
        "value": 0.002,
        "color": "#000000",
        "alpha": 0.0
    },
    {
        "value": 0.005,
        "color": "#8e0101",
        "alpha": 0.25
    },
    {
        "value": 0.01,
        "color": "#cf2200",
        "alpha": 0.75
    },
    {
        "value": 0.02,
        "color": "#e38400"
    },
    {
        "value": 0.05,
        "color": "#e3df00"
    },
    {
        "value": 0.1,
        "color": "#a6e300"
    },
    {
        "value": 0.2,
        "color": "#62e300"
    },
    {
        "value": 0.3,
        "color": "#00e32d"
    },
    {
        "value": 0.4,
        "color": "#00e384"
    },
    {
        "value": 0.5,
        "color": "#00e3c8"
    },
    {
        "value": 0.6,
        "color": "#00c5e3"
    },
    {
        "value": 0.7,
        "color": "#0097e3"
    },
    {
        "value": 0.8,
        "color": "#005fe3"
    },
    {
        "value": 0.9,
        "color": "#000fe3"
    },
    {
        "value": 1.0,
        "color": "#5700e3"
    }
]

__clear_ramp_values__ = [
    {
        "value": 0,
        "color": "#FFFFFF",
        "alpha": 0
    },
    {
        "value": 10,
        "color": "#B21800"
    },
    {
        "value": 25,
        "color": "#FF4400"
    },
    {
        "value": 50,
        "color": "#FF8000"
    },
    {
        "value": 100,
        "color": "#FFA200"
    },
    {
        "value": 150,
        "color": "#FFC000"
    },
    {
        "value": 200,
        "color": "#FFD500"
    },
    {
        "value": 250,
        "color": "#FFF300"
    },
    {
        "value": 300,
        "color": "#E6FF00"
    },
    {
        "value": 350,
        "color": "#BCFF00"
    },
    {
        "value": 400,
        "color": "#89FF00"
    },
    {
        "value": 500,
        "color": "#68C400"
    },
    {
        "value": 600,
        "color": "#44C400"
    },
    {
        "value": 700,
        "color": "#03B500"
    },
    {
        "value": 800,
        "color": "#039500"
    },
    {
        "value": 1000,
        "color": "#026900"
    }
]

__water_ramp_values__ = [
    {
        "value": 0,
        "color": "#666666",
        "alpha": 0
    },
    {
        "value": 2,
        "color": "#890000"
    },
    {
        "value": 5,
        "color": "#990000"
    },
    {
        "value": 10,
        "color": "#E38400"
    },
    {
        "value": 25,
        "color": "#E3DF00"
    },
    {
        "value": 50,
        "color": "#A6E300"
    },
    {
        "value": 100,
        "color": "#00E32D"
    },
    {
        "value": 150,
        "color": "#00E3C8"
    },
    {
        "value": 200,
        "color": "#0097E3"
    },
    {
        "value": 250,
        "color": "#005FE3"
    },
    {
        "value": 300,
        "color": "#000FE3"
    },
    {
        "value": 350,
        "color": "#000EA9"
    },
    {
        "value": 400,
        "color": "#5700E3"
    }
]

def __generate_color_ramp__(ramp_values, delta):
    def frange(start, stop, step):
        i = start
        while i < stop:
            yield i
            i += step
    from colour import Color
    values = []
    ramp = []
    alpha = []
    low = None
    high = None
    for i, pair in enumerate(ramp_values):
        if i == 0:
            low = pair
            continue
        high = pair
        prev = len(values)
        alpha_low = low.get("alpha", 1.0)
        alpha_high = high.get("alpha", 1.0)
        values.extend(frange(low["value"], high["value"], delta))
        if alpha_high != alpha_low:
            alpha_range = frange(alpha_low, alpha_high, (alpha_high - alpha_low) / delta)
        else:
            alpha_range = [1.0 for i in range(len(values))]
        ramp.extend(Color(low["color"]).range_to(Color(high["color"]), len(values) - prev))
        alpha.extend(alpha_range)
        low = pair
    return zip(values, ramp, alpha)

__wofs_summary_ramp__ = __generate_color_ramp__(__ramp_values__, 0.01)
__clear_summary_ramp__ = __generate_color_ramp__(__clear_ramp_values__, 5)
__water_summary_ramp__ = __generate_color_ramp__(__water_ramp_values__, 1)

def __get_calculate_summary_ramp__(ramp_values, ramp_colors, ramp_alpha):
    def calculate_ramp(data, band, imgband):
        def process(values, colors, alpha, imgband, data):
            i = bisect(values, data)
            i = i if i < len(colors) else i - 1
            c = colors[i]
            a = alpha[i]
            val = a if imgband is "alpha" else getattr(c, imgband)
            return (val * 255.0)

        p = partial(process, ramp_values, ramp_colors, ramp_alpha, imgband)

        ramped = data.copy(deep=True)
        ramped.values = np.vectorize(p)(data.values)
        return ramped

    return calculate_ramp

__calculate_wofs_summary_ramp__ = __get_calculate_summary_ramp__(*zip(*__wofs_summary_ramp__))
__calculate_wofs_clear_ramp__ = __get_calculate_summary_ramp__(*zip(*__clear_summary_ramp__))
__calculate_wofs_water_ramp__ = __get_calculate_summary_ramp__(*zip(*__water_summary_ramp__))


layer_cfg = [
    # Layer Config is a list of platform configs
    {
        "name": "fractional cover",
        "title": "Fractional Cover",
        "abstract": "Fractional Cover",
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "FC",
                # Included as a keyword  for the layer
                "type": "fractional cover",
                # Included as a keyword  for the layer
                "variant": "terrain corrected",
                # The WMS name for the layer
                "name": "ls8_fc_albers",
                # The Datacube name for the associated data product
                "product_name": "ls8_fc_albers",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                "pq_dataset": "wofs_albers",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                "pq_band": "water",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 500.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],

                "styles": [
                    {
                        "name": "simple_fc",
                        "title": "Fractional Cover",
                        "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
                        "components": {
                            "red": {
                                "BS": 1.0
                            },
                            "green": {
                                "PV": 1.0
                            },
                            "blue": {
                                "NPV": 1.0
                            }
                        },
                        # Used to clip off very bright areas.
                        "scale_factor": 0.39,
                        "pq_masks": [
                            {
                                "flags": {
                                    'dry': True
                                },
                            },
                            {
                                "flags": {
                                    "terrain_or_low_angle": False,
                                    "high_slope": False,
                                    "cloud_shadow": False,
                                    "cloud": False,
                                    "sea": False
                                }
                            },
                        ]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_fc",
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Geomedian_AU_NBART",
        "title": "Geomedian_au_nbart_surface_reflectance",
        "abstract": "Images from the Geomedian Surface Reflectance on Level2 Products",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
            # Included as a keyword  for the layer
                "label": "LANDSAT_8",
                # Included as a keyword  for the layer
                "type": "SR",
                # Included as a keyword  for the layer
                "variant": "Level 2",
                # The WMS name for the layer
                "name": "ls8_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls8_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 0.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],
               
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infra_red",
                        "title": "False colour multi-band infra-red",
                        "abstract": "Simple false-colour image, using the near and short-wave infra-red bands",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour SWIR, NIR and green",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Spectral band 2 - Blue",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Spectral band 3 - Green",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Spectral band 4 - Red",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Spectral band 5 - Near infra-red",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Spectral band 6 - Short wave infra-red 1",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Spectral band 7 - Short wave infra-red 2",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        # Areas where the index_function returns outside the range are masked.
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["green"] - data["nir"]) / (data["nir"] + data["green"]),
                        "needed_bands": ["green", "nir"],
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "ndbi",
                        "title": "NDBI",
                        "abstract": "Normalised Difference Buildup Index - a derived index that correlates with the existence of urbanisation",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["swir2"] - data["nir"]) / (data["swir2"] + data["nir"]),
                        "needed_bands": ["swir2", "nir"],
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "rgb_ndvi",
                        "title": "NDVI plus RGB",
                        "abstract": "Normalised Difference Vegetation Index (blended with RGB) - a derived index that correlates well with the existence of vegetation",
                        "component_ratio": 0.6,
                        "heat_mapped": True,
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        # Areas where the index_function returns outside the range are masked.
                        "range": [0.0, 1.0],
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "LANDSAT_7",
                # Included as a keyword  for the layer
                "type": "SR",
                # Included as a keyword  for the layer
                "variant": "Level 2",
                # The WMS name for the layer
                "name": "ls7_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls7_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 0.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infra_red",
                        "title": "False colour multi-band infra-red",
                        "abstract": "Simple false-colour image, using the near and short-wave infra-red bands",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour SWIR, NIR and green",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Spectral band 2 - Blue",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Spectral band 3 - Green",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Spectral band 4 - Red",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Spectral band 5 - Near infra-red",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Spectral band 6 - Short wave infra-red 1",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Spectral band 7 - Short wave infra-red 2",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        # Areas where the index_function returns outside the range are masked.
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["green"] - data["nir"]) / (data["nir"] + data["green"]),
                        "needed_bands": ["green", "nir"],
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "ndbi",
                        "title": "NDBI",
                        "abstract": "Normalised Difference Buildup Index - a derived index that correlates with the existence of urbanisation",
                        "heat_mapped": True,
                        "index_function": lambda data: (data["swir2"] - data["nir"]) / (data["swir2"] + data["nir"]),
                        "needed_bands": ["swir2", "nir"],
                        "range": [0.0, 1.0],
                    },
                    {
                        "name": "rgb_ndvi",
                        "title": "NDVI plus RGB",
                        "abstract": "Normalised Difference Vegetation Index (blended with RGB) - a derived index that correlates well with the existence of vegetation",
                        "component_ratio": 0.6,
                        "heat_mapped": True,
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        # Areas where the index_function returns outside the range are masked.
                        "range": [0.0, 1.0],
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "LANDSAT_5",
                # Included as a keyword  for the layer
                "type": "SR",
                # Included as a keyword  for the layer
                "variant": "Level 2",
                # The WMS name for the layer
                "name": "ls5_nbart_geomedian_annual",
                # The Datacube name for the associated data product
                "product_name": "ls5_nbart_geomedian_annual",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 0.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infra_red",
                        "title": "False colour multi-band infra-red",
                        "abstract": "Simple false-colour image, using the near and short-wave infra-red bands",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour SWIR, NIR and green",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "blue",
                        "title": "Spectral band 2 - Blue",
                        "abstract": "Blue band, approximately 453nm to 511nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Spectral band 3 - Green",
                        "abstract": "Green band, approximately 534nm to 588nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Spectral band 4 - Red",
                        "abstract": "Red band, roughly 637nm to 672nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Spectral band 5 - Near infra-red",
                        "abstract": "Near infra-red band, roughly 853nm to 876nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Spectral band 6 - Short wave infra-red 1",
                        "abstract": "Short wave infra-red band 1, roughly 1575nm to 1647nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Spectral band 7 - Short wave infra-red 2",
                        "abstract": "Short wave infra-red band 2, roughly 2117nm to 2285nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "rgb_ndvi",
                        "title": "NDVI plus RGB",
                        "abstract": "Normalised Difference Vegetation Index (blended with RGB) - a derived index that correlates well with the existence of vegetation",
                        "component_ratio": 0.6,
                        "heat_mapped": True,
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        # Areas where the index_function returns outside the range are masked.
                        "range": [0.0, 1.0],
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            }
        ]
    },
    {
        "name": "mangrove_cover",
        "title": "Mangrove Cover",
        "abstract": "Mangrove Cover",
        "products": [
            {
                "label": "Mangrove Cover",
                "type": "Level3",
                "variant": "Level 3",
                "name": "mangrove_cover",
                "product_name": "mangrove_cover",
                "min_zoom_factor": 0.0,
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                "time_zone": 9,
                "extent_mask_func": lambda data, band: data["extent"] == 1,
                "ignore_info_flags": [],
                "data_manual_merge": False,
                "always_fetch_bands": ["extent"],
                "apply_solar_corrections": False,
                "styles": [
                    {
                        "name": "mangrove",
                        "title": "Mangrove Cover",
                        "abstract": "Mangrove Cover",
                        "value_map": {
                            "canopy_cover_class": [
                                {
                                    "flags": {
                                        "woodland": True
                                    },
                                    "values": {
                                        "red": 159,
                                        "green": 255,
                                        "blue": 76
                                    }
                                },
                                {
                                    "flags": {
                                        "open_forest": True
                                    },
                                    "values": {
                                        "red": 94,
                                        "green": 204,
                                        "blue": 0
                                    }
                                },
                                {
                                "flags": {
                                        "closed_forest": True
                                    },
                                    "values": {
                                        "red": 59,
                                        "green": 127,
                                        "blue": 0
                                    }
                                },
                            ]
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "mangrove",
            },
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "WOfS",
        "title": "Water_Observation_from_Space",
        "abstract": "WOfS",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
            # Included as a keyword  for the layer
                "label": "WOFLs",
                # Included as a keyword  for the layer
                "type": "albers",
                # Included as a keyword  for the layer
                "variant": "wofs",
                # The WMS name for the layer
                "name": "wofs_albers",
                # The Datacube name for the associated data product
                "product_name": "wofs_albers",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls8_level1_usgs",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_manual_data_merge": True,
                # "data_manual_merge": True,
                # "pq_band": "quality",
                "pq_band": "water",
                # "always_fetch_bands": [ "quality" ],
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 500.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [200, 180, 180, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],
                "pq_manual_merge": True,
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [
                    "nodata",
                    "noncontiguous",
                ],
                "data_manual_merge": False,
                "always_fetch_bands": [ ],
                "apply_solar_corrections": False,
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "water",
                        "title": "Water",
                        "abstract": "Water",
                        "value_map": {
                            "water": [
                                {
                                    "flags": {
                                        "wet": True,
                                    },
                                    "values": {
                                        "red": 79,
                                        "green": 129,
                                        "blue": 189
                                    }
                                },
                                {
                                    "flags": {
                                        "sea": True,
                                    },
                                    "values": {
                                        "red": 79,
                                        "green": 129,
                                        "blue": 189
                                    }
                                },
                                {
                                    "flags": {
                                        "dry": True,
                                    },
                                    "values": {
                                        "red": 217,
                                        "green": 150,
                                        "blue": 148
                                    }
                                },
                                {
                                    "flags": {
                                        "terrain_or_low_angle": True,
                                    },
                                    "values": {
                                        "red": 112,
                                        "green": 112,
                                        "blue": 112
                                    }
                                },
                                {
                                    "flags": {
                                        "high_slope": True,
                                    },
                                    "values": {
                                        "red": 112,
                                        "green": 112,
                                        "blue": 112
                                    }
                                },
                                {
                                    "flags": {
                                        "cloud_shadow": True,
                                    },
                                    "values": {
                                        "red": 112,
                                        "green": 112,
                                        "blue": 112
                                    }
                                },
                                {
                                    "flags": {
                                        "cloud": True
                                    },
                                    "values": {
                                        "red": 112,
                                        "green": 112,
                                        "blue": 112
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "name": "water_masked",
                        "title": "Water (Masked)",
                        "abstract": "Water Data, Masked",
                        # Invert True: Show if no flags match
                        "value_map": {
                            "water": [
                                {
                                    "flags": {
                                        "wet": True
                                    },
                                    "values": {
                                        "red": 79,
                                        "green": 129,
                                        "blue": 189
                                    }
                                },
                            ]
                        },
                        "pq_masks": [
                            {
                                "flags": {
                                    'wet': True,
                                },
                            },
                        ],
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "water",

            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS_Summary",
                # Included as a keyword  for the layer
                "type": "WOfS_Summary",
                # Included as a keyword  for the layer
                "variant": "Summary",
                # The WMS name for the layer
                "name": "wofs_summary",
                # The Datacube name for the associated data product
                "product_name": "wofs_summary",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                #"pq_dataset": "wofs_albers",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                #"pq_band": "water",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 0.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],

                "styles": [
                    {
                        "name": "WOfS_frequency",
                        "title": " Wet and Dry Count",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "components": {
                            "red": {
                                "frequency": __calculate_wofs_summary_ramp__
                            },
                            "green": {
                                "frequency": __calculate_wofs_summary_ramp__
                            },
                            "blue": {
                                "frequency": __calculate_wofs_summary_ramp__
                            },
                            "alpha": {
                                "frequency": __calculate_wofs_summary_ramp__
                            }
                        },
                        "scale_range": [ 0, 255 ],
                    },
                    {
                        "name": "clear_observations",
                        "title": "Clear Observations Count",
                        "abstract": "WOfS summary showing the count of clear observations",
                        "needed_bands": ["count_clear"],
                        "components": {
                            "red": {
                                "count_clear": __calculate_wofs_clear_ramp__
                            },
                            "green": {
                                "count_clear": __calculate_wofs_clear_ramp__
                            },
                            "blue": {
                                "count_clear": __calculate_wofs_clear_ramp__
                            },
                            "alpha": {
                                "count_clear": __calculate_wofs_clear_ramp__
                            }
                        },
                        "scale_range": [ 0, 255 ],
                    },
                    {
                        "name": "water_observations",
                        "title": "Water Observations Count",
                        "abstract": "WOfS summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "components": {
                            "red": {
                                "count_wet": __calculate_wofs_water_ramp__
                            },
                            "green": {
                                "count_wet": __calculate_wofs_water_ramp__
                            },
                            "blue": {
                                "count_wet": __calculate_wofs_water_ramp__
                            },
                            "alpha": {
                                "count_wet": __calculate_wofs_water_ramp__
                            }
                        },
                        "scale_range": [ 0, 255 ],
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "WOfS_frequency",
            }

        ],
    },

]
