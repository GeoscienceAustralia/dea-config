# Static config for the wms metadata.

response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    ## Which web service(s) should be supported by this instance
    "wcs": False,
    "wms": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "WMS server for Water Observation from Space",
    # Service URL.  Should a fully qualified URL
    "url": "https://ows.wms.gadevs.ga",

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
        "wofs"
        "wofls",
        "wofs_summary",
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

def __generate_color_ramp__():
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
    for i, pair in enumerate(__ramp_values__):
        if i == 0:
            low = pair
            continue
        high = pair
        prev = len(values)
        alpha_low = low.get("alpha", 1.0)
        alpha_high = high.get("alpha", 1.0)
        values.extend(frange(low["value"], high["value"], 0.01))
        if alpha_high != alpha_low:
            alpha_range = frange(alpha_low, alpha_high, (alpha_high - alpha_low) / 0.01)
        else:
            alpha_range = [1.0 for i in range(len(values))]
        ramp.extend(Color(low["color"]).range_to(Color(high["color"]), len(values) - prev))
        alpha.extend(alpha_range)
        low = pair
    return zip(values, ramp, alpha)

__wofs_summary_ramp__ = __generate_color_ramp__()
__wofs_ramp_values__, __wofs_ramp_colors__, __wofs_ramp_alpha__ = zip(*__wofs_summary_ramp__)

def __calculate_wofs_summary_ramp__(data, band, imgband):
    from colour import Color
    from bisect import bisect
    from functools import partial
    import xarray
    import numpy as np
    def process(values, colors, alpha, imgband, data):
        i = bisect(values, data)
        i = i if i < len(colors) else i - 1
        c = colors[i]
        a = alpha[i]
        val = a if imgband is "alpha" else getattr(c, imgband)
        return (val * 255.0)

    p = partial(process, __wofs_ramp_values__, __wofs_ramp_colors__, __wofs_ramp_alpha__, imgband)

    ramped = data.copy(deep=True)
    ramped.values = np.vectorize(p)(data.values)
    return ramped


layer_cfg = [
    # Layer Config is a list of platform configs
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
                "extent_mask_func": lambda data, band: ((data['frequency'] >= 0.01).astype('bool') & (data['frequency'] != data['frequency'].attrs['nodata']).astype('bool')),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],

                "styles": [
                    {
                        "name": "WOfS_frequency",
                        "title": " Wet and Dry Count",
                        "abstract": "WOfS summary determinig the count_wet and count_clear for WOfS product",
                        "needed_bands": ["frequency"],
                        "scale_range": [0.01, 1.0],
                        "components": {
                            "red": {
                                "frequency": 0.0
                            },
                            "green": {
                                "frequency": 0.0
                            },
                            "blue": {
                                "frequency": 1.0
                            }
                        },
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
    "extent_mask_func": lambda data, band: (data['frequency'] != data['frequency'].attrs['nodata']),
    # Flags listed here are ignored in GetFeatureInfo requests.
    # (defaults to empty list)
    "ignore_info_flags": [],

    "styles": [
        {
            "name": "WOfS_frequency",
            "title": " Wet and Dry Count",
            "abstract": "WOfS summary determinig the count_wet and count_clear for WOfS product",
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
        }
    ],
    # Default style (if request does not specify style)
    # MUST be defined in the styles list above.

    # (Looks like Terria assumes this is the first style in the list, but this is
    #  not required by the standard.)
    "default_style": "WOfS_frequency",
}
]
