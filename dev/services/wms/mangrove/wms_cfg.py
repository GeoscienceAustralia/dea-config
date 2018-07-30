response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
    "Cache-Control": "public, max-age=3600"
}

service_cfg = {
    # Required config
    "title": "WMS server for Mangrove Cover",
    "url": "https://mangrove.wms.gadevs.ga",
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
                "min_zoom_factor": 500.0,
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
]
