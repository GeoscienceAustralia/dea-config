response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
    "Cache-Control": "public, max-age=3600"
}

service_cfg = {
    # Required config
    "title": "WMS server for Fractional Cover",
    "url": "https://fc.wms.gadevs.ga",
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
            "horizontal_coord": "easting",
            "vertical_coord": "northing",
        },
    },

    "layer_limit": 1,
    "max_width": 512,
    "max_height": 512,

    "abstract": """Historic Landsat imagery for Australia.""",
    "keywords": [
        "Geomedian",
        "australia",
        "time-series",
    ],
    "contact_info": {
        "person": "Digital Earth Australia",
        "organisation": "Geoscience Australia",
        "position": "Technical Lead",
        "address": {
            "type": "postal",
            "address": "GPO Box 378",
            "city": "Canberra",
            "state": "ACT",
            "postcode": "2906",
            "country": "Australia",
        },
        "telephone": "",
        "fax": "",
        "email": "",
    },
    "fees": "",
    "access_constraints": "",
    "wcs_formats": {
        "GeoTIFF": {
            "renderer": "datacube_wms.wcs_utils.get_tiff",
            "mime": "image/geotiff",
            "extension": "tif",
            "multi-time": False
        },
        "netCDF": {
            "renderer": "datacube_wms.wcs_utils.get_netcdf",
            "mime": "application/x-netcdf",
            "extension": "nc",
            "multi-time": True,
        }
    },
    "native_wcs_format": "GeoTIFF",
}
layer_cfg = [
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
            "zoomed_out_fill_colour": [ 150, 180, 200, 160],
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
    }
]
